import pygame
from config import *
from sprites_personaje import *
from class_moneda import *
from class_booster import *
from pygame import mixer

class Spidey(pygame.sprite.Sprite):
    def __init__(self, tamaño:tuple, animaciones:dict, posicion_inicial:tuple, velocidad:int):
        super().__init__()
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.size = (self.ancho,self.alto)
        #VELOCIDAD
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #GRAVEDAD 
        self.gravedad = 2
        self.potencia = -25
        self.limite_vel_caida = 25
        self.esta_saltando = False
        self.saltos_realizados = 2 
        #NIVEL GANADO
        self.siguiente_nivel = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.image = self.animaciones["camina_derecha"][0]
        self.reescalar_animaciones()
        self.izquierda = False
        self.derecha = True
        #RECTANGULOS
        self.rect = self.image.get_rect()
        self.rect.x = posicion_inicial[0]
        self.rect.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rect)
        self.colision = False
        #proyectiles
        self.cooldown_proyectil = 0
        #vida
        self.vida_actual = 900
        self.vida_maxima = 900
        self.target_vida = 900
        self.estado_vida = False
        #barra
        self.barra_vida = 300
        self.proporcion_vida = self.vida_maxima / self.barra_vida
        self.vida_cambio_velocidad = 5
        #monedas
        self.puntaje = 0
        self.monedas = 0
        self.puntaje_anterior = 0
        self.puntaje_mas_alto = 0
        self.coin_play = mixer.Sound("./src/recursos/sonidos/Coin.wav")
        self.power_up_play = mixer.Sound("./src/recursos/sonidos/Powerup.wav")
        self.kick_play = mixer.Sound("./src/recursos/sonidos/Kick.wav")

    def recibir_daño(self,cantidad):
        if self.target_vida > 0:
            self.target_vida -= cantidad
        if self.target_vida < 0:
            self.target_vida = 0
    
    def recibir_vida(self,cantidad):
        if self.target_vida < self.vida_maxima:
            self.target_vida += cantidad
        if self.target_vida >= self.vida_maxima:
            self.target_vida = self.vida_maxima
    
    def generar_barra_vida(self,pantalla):
        ancho_transicion = 0
        color_transicion = (255,0,0)

        if self.vida_actual < self.target_vida:
            self.vida_actual += self.vida_cambio_velocidad
            ancho_transicion = (self.target_vida - self.vida_actual) / self.proporcion_vida
            color_transicion = (0,255,0)
        if self.vida_actual > self.target_vida:
            self.vida_actual -= self.vida_cambio_velocidad
            ancho_transicion = (self.target_vida - self.vida_actual) / self.proporcion_vida
            color_transicion = (255,255,0)
        
        largo_barra = self.vida_actual/self.proporcion_vida 
        rectangulo_barra = pygame.Rect(10,20,largo_barra,20)
        rectangulo_barra_transicion = pygame.Rect(rectangulo_barra.right,20,ancho_transicion,20)

        pygame.draw.rect(pantalla,(255,0,0),rectangulo_barra)
        pygame.draw.rect(pantalla,color_transicion,rectangulo_barra_transicion)
        pygame.draw.rect(pantalla,(255,255,255),(10,20,self.barra_vida,20),4)

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.size)
        
    def animar_personaje(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1 
    
    def animar_una_vez(self,pantalla,que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos < largo - 2:
            self.contador_pasos += 1
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        
    def mover_personaje(self,velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def saltar(self):
        self.desplazamiento_y = self.potencia
        self.saltos_realizados += 1


    def aplicar_gravedad(self,pantalla,lista_plataformas):
        if self.esta_saltando:
            self.animar_personaje(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_vel_caida:
                self.desplazamiento_y += self.gravedad

        for plat in lista_plataformas:
            if self.lados['top'].colliderect(plat.lados["bottom"]):
                self.desplazamiento_y += self.gravedad
            if self.lados['bottom'].colliderect(plat.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.saltos_realizados = 2
                self.lados['main'].bottom = plat.lados['main'].top + 3
                break
            else:
                self.esta_saltando = True

    def direction(self):
        if self.derecha:
            return 1
        elif self.izquierda:
            return -1
        
    def cooldown(self):
        if self.cooldown_proyectil  >= 15:
            self.cooldown_proyectil  = 0
        elif self.cooldown_proyectil  > 0:
            self.cooldown_proyectil  += 1


    def crear_proyectil(self):
        return Telaraña(tamaño_proyectil,velocidad_proyectil,personaje_telaraña,(self.lados["main"].x,self.lados["main"].y),self.direction())
    
    def crear_moneda(self,coordenadas:tuple):
        return Coin(tamaño_moneda,moneda,coordenadas)
    
    def crear_booster(self,coordenadas):
        return Booster(hongo_rojo,coordenadas)
    
    def draw_puntaje(self,font,pantalla):
        name = font.render("SPIDEY", True, "White")
        puntaje = font.render(str(self.puntaje) , True, "White")
        x = font.render("X" , True, "Orange")
        moneda_score = font.render(str(self.monedas) , True, "White")

        pantalla.blit(name,(700,10))
        pantalla.blit(puntaje,(720,30))
        pantalla.blit(x,(950,20))
        pantalla.blit(moneda_score,(972,20))


    def hit_collision(self,g_enemigos,g_sorpresa,g_ordinarias,g_moneda,g_booster,g_hongo,g_escalera,all_plat,g_next):
        #colision con enemigo
        for enemigo in g_enemigos:
            if self.lados["bottom"].colliderect(enemigo.lados["top"]):
                self.kick_play.play()
                self.puntaje += 300
                enemigo.vida = False
            elif self.lados["right"].colliderect(enemigo.lados["main"]):
                    self.recibir_daño(100)
        #colision con cajas sorpresa  
        for plat in g_sorpresa:
            if plat.golpeado == False:
                if self.lados["top"].colliderect(plat.lados["bottom"]):
                    plat.golpeado = True
                    coordenadas = (plat.rect.x+5,plat.rect.y - 80)
                    g_moneda.add(self.crear_moneda(coordenadas))
        #colision con caja con booster
        for plat in g_booster:
            if plat.golpeado == False:
                if self.lados["top"].colliderect(plat.lados["bottom"]):
                    plat.golpeado = True
                    coordenadas = (plat.rect.x+5,plat.rect.y - 80)
                    g_hongo.add(self.crear_booster(coordenadas))
        #colision con booster hongo
        for hongo in g_hongo:
            if self.lados["main"].colliderect(hongo.lados["main"]):
                self.power_up_play.play()
                self.puntaje += 1000
                self.recibir_vida(300)
                hongo.kill()
        #colision con caja comun
        for plat in g_ordinarias:
            if self.lados["top"].colliderect(plat.lados["bottom"]):
                plat.kill()
        #colision con moneda
        for moneda in g_moneda:
            if self.lados["main"].colliderect(moneda.lados["main"]):
                self.coin_play.play()
                self.puntaje += 100
                self.monedas += 1
                moneda.kill()
        #colision con escalera
        for escalera in g_escalera:
            if (self.lados["main"].colliderect(escalera.lados["left"])) or (self.lados["main"].colliderect(escalera.lados["right"])):
                self.colision = True
        for plat in all_plat:
            if self.lados["top"].colliderect(plat.lados["bottom"]):
                if self.desplazamiento_y < 0:
                    self.lados["main"].top = plat.lados["main"].bottom 
                    self.desplazamiento_y *= -1
            if self.lados["left"].colliderect(plat.lados["right"]):
                self.lados["main"].left = plat.lados["main"].right 
                self.colision = True
            if self.lados["right"].colliderect(plat.lados["left"]):
                self.lados["main"].right = plat.lados["main"].left 
                self.colision = True
            if self.lados["bottom"].colliderect(plat.lados["top"]):
                self.lados['main'].bottom = plat.lados['main'].top 
                self.colision = False
        for plat in g_next:
            if self.lados["main"].colliderect(plat.lados["main"]):
                self.siguiente_nivel = True

    def resetear_vida(self):
        self.vida_actual = 900
        self.estado_vida = False

    def accion(self,pantalla):
        match self.que_hace:
            case "derecha":
                self.derecha = True
                self.izquierda =  False
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"camina_derecha")
                self.mover_personaje(self.velocidad)
                print("aaa")
            case "izquierda":
                self.izquierda =  True
                self.derecha = False
                if not self.esta_saltando: 
                    self.animar_personaje(pantalla,"camina_izquierda")
                self.mover_personaje(- 1 * self.velocidad  )
            case "salta":
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia
            case "defensa" :
                if not self.esta_saltando: 
                    self.animar_una_vez(pantalla, "personaje_defensa" )  
            case "dispara" : 
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"personaje_ataca")
            case "quieto": 
                if not self.esta_saltando:
                    if self.derecha:
                        self.animar_personaje(pantalla, "quieto_derecha" )
                    elif self.izquierda:
                        self.animar_personaje(pantalla, "quieto_izquierda" )  

    def esta_vivo(self):
        if self.vida_actual == 0 or (self.lados["main"].y < -100 or self.lados["main"].y > HEIGHT ):
            self.estado_vida = True

    def update(self,pantalla,g_enemigos,g_plataformas,g_sorpresa,g_ordinarias,g_moneda,g_booster,g_hongo,g_escalera,all_plat,g_next):
        self.cooldown()
        self.accion(pantalla)
        self.esta_vivo()
        self.aplicar_gravedad(pantalla,g_plataformas)
        self.hit_collision(g_enemigos,g_sorpresa,g_ordinarias,g_moneda,g_booster,g_hongo,g_escalera,all_plat,g_next)
        self.generar_barra_vida(pantalla)
        self.draw_puntaje(font,pantalla)


class Telaraña(pygame.sprite.Sprite):
    def __init__(self, tamaño, velocidad,personaje_telaraña,posicion_actual,direction):
        super().__init__()

        #Confeccion
        self.ancho = tamaño
        self.alto = tamaño
        self.size = (self.ancho,self.alto)
        #velocidad
        self.velocidad = velocidad
        #Rectangulos
        self.image = personaje_telaraña[0]
        self.rect= self.image.get_rect()
        self.rect.x = posicion_actual[0]
        self.rect.y = posicion_actual[1] + 28
        self.lados = obtener_rectangulos(self.rect)
        self.direction = direction
        

    def reescalar_animaciones(self):
        reescalar_imagenes(self.image, self.size)

    def mover(self,velocidad):
        if self.direction == 1:
            self.lados["main"].x += velocidad 
        elif self.direction == -1:
            self.lados["main"].x -= velocidad + 20
    
    
    def off_screen(self):
        if self.lados["main"].x >= WIDTH + 100:
            self.kill()

    def hit_collision(self,g_proyectil,enemigo,personaje):
        for proyectil in g_proyectil:
                lista = pygame.sprite.spritecollide(proyectil,enemigo,True)
                if len(lista) != 0:
                    self.kill()
                    enemigo.vida = False
                    personaje.puntaje += 300

    def update(self,velocidad,g_proyectil,enemigo,personaje):
        self.mover(velocidad)
        self.hit_collision(g_proyectil,enemigo,personaje)


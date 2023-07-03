import pygame
from config import *
from sprites_personaje import *
from class_moneda import *



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
        self.potencia = -15
        self.limite_vel_caida = 15
        self.esta_saltando = False
        self.saltos = 2
        self.saltos_actuales = self.saltos
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
        #proyectiles
        self.cooldown_proyectil = 0
        #vida
        self.vida_actual = 1000
        self.vida_maxima = 1000
        self.target_vida = 1000
        #barra
        self.barra_vida = 400
        self.proporcion_vida = self.vida_maxima / self.barra_vida
        self.vida_cambio_velocidad = 5

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
    
    def vida_basica(self,pantalla):
        largo_barra = self.target_vida/self.proporcion_vida
        pygame.draw.rect(pantalla,(255,0,0),(10,10,largo_barra,25))
        pygame.draw.rect(pantalla,(255,255,255),(10,10,self.barra_vida,25),4)
    
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
        
        largo_barra = self.vida_actual/self.proporcion_vida +1
        rectangulo_barra = pygame.Rect(10,45,largo_barra,25)
        rectangulo_barra_transicion = pygame.Rect(rectangulo_barra.right,45,ancho_transicion,25)

        pygame.draw.rect(pantalla,(255,0,0),rectangulo_barra)
        pygame.draw.rect(pantalla,color_transicion,rectangulo_barra_transicion)
        pygame.draw.rect(pantalla,(255,255,255),(10,45,self.barra_vida,25),4)

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
    
    def aplicar_gravedad(self,pantalla,lista_plataformas):
        if self.esta_saltando:
            self.animar_personaje(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_vel_caida:
                self.desplazamiento_y += self.gravedad
                
        for plat in lista_plataformas:
            if self.lados['bottom'].colliderect(plat.lados["top"]):
                self.desplazamiento_y = 0
                self.saltos_actuales = self.saltos
                self.esta_saltando = False
                self.lados['main'].bottom = plat.lados['main'].top -2
                break
            else:
                self.esta_saltando = True

    def direction(self):
        if self.derecha:
            return 1
        elif self.izquierda:
            return -1
        
    def cooldown(self):
        if self.cooldown_proyectil > 0:
            self.cooldown_proyectil -= 1

    def crear_proyectil(self):
        self.cooldown()
        return Telaraña(tamaño_proyectil,velocidad_proyectil,personaje_telaraña,(self.lados["main"].x,self.lados["main"].y),self.direction())
    
    def crear_moneda(self,coordenadas:tuple):
        return Coin(tamaño_moneda,modeda,coordenadas)
    
    def hit_collision(self,g_enemigos,g_sorpresa,g_ordinarias,g_moneda):
        for enemigo in g_enemigos:
            if self.lados["bottom"].colliderect(enemigo.lados["top"]):
                enemigo.kill()
            elif self.lados["right"].colliderect(enemigo.lados["left"]):
                print("tocado")
                self.recibir_daño(200)
        for plat in g_sorpresa:
            if self.lados["top"].colliderect(plat.lados["bottom"]):
                plat.golpeado = True
                coordenadas = (plat.rect.x+5,plat.rect.y - 80)
                g_moneda.add(self.crear_moneda(coordenadas))
        for plat in g_ordinarias:
            if self.lados["top"].colliderect(plat.lados["bottom"]):
                plat.kill()
            

        # for enemigo in g_enemigos:
        #     lista_impactos = pygame.sprite.spritecollide(enemigo,g_player,True)
        #     if len(lista_impactos) == 3:
        #         print("game over")
        #     for i in lista_impactos:
        #         self.vidas -= 1 
        #         print(self.vidas)

    def update(self,pantalla,g_enemigos,g_plataformas,g_sorpresa,g_ordinarias,g_moneda):
        match self.que_hace:
            case "derecha":
                self.derecha = True
                self.izquierda =  False
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"camina_derecha")
                self.mover_personaje(self.velocidad)
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
        self.aplicar_gravedad(pantalla,g_plataformas)
        self.hit_collision(g_enemigos,g_sorpresa,g_ordinarias,g_moneda)
        self.generar_barra_vida(pantalla)


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
        self.rect.y = posicion_actual[1] + 10
        self.lados = obtener_rectangulos(self.rect)
        self.direction = direction
        

    def reescalar_animaciones(self):
        reescalar_imagenes(self.image, self.size)

    def mover(self,velocidad):
        if self.direction == 1:
            self.lados["main"].x += velocidad 
        elif self.direction == -1:
            self.lados["main"].x -= velocidad 
        
    
    def off_screen(self):
        if self.lados["main"].x >= WIDTH + 100:
            self.kill()

    
    def hit_collision(self,g_proyectil,enemigo):
        for proyectil in g_proyectil:
            if not self.off_screen():
                lista = pygame.sprite.spritecollide(proyectil,enemigo,True)
                if len(lista) != 0:
                    self.kill()
                    enemigo.vida = True

    def update(self,velocidad,g_proyectil,enemigo):
        self.mover(velocidad)
        self.hit_collision(g_proyectil,enemigo)


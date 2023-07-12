import pygame

from config import *
from funciones import *

enemigo_donkey_izq = [pygame.image.load("./src/recursos/nivel_2/donkey/2.png")]

enemigo_donkey_der = [pygame.image.load("./src/recursos/nivel_2/donkey/4.png")]

enemigo_donkey_barril = [pygame.image.load("./src/recursos/nivel_2/donkey/7.png"),
                        pygame.image.load("./src/recursos/nivel_2/donkey/3.png")]


enemigo_goomba_izq = [pygame.image.load("./src/recursos/bichos/0.png"),
        pygame.image.load("./src/recursos/bichos/1.png"),
        pygame.image.load("./src/recursos/bichos/2.png"),
        pygame.image.load("./src/recursos/bichos/2 - copia.png")
        ]

enemigo_goomba_der = girar_imagenes(enemigo_goomba_izq,True,False)

enemigo_tortuga_izq = [pygame.image.load("./src/recursos/bichos/3.png"),
        pygame.image.load("./src/recursos/bichos/4.png"),
        pygame.image.load("./src/recursos/bichos/5.png"),
        pygame.image.load("./src/recursos/bichos/6.png"),
        ]
enemigo_tortuga_der = girar_imagenes(enemigo_tortuga_izq,True,False)

animaciones_tortuga = {}
animaciones_tortuga["derecha"] = enemigo_tortuga_der
animaciones_tortuga["izquierda"] = enemigo_tortuga_izq

animaciones_goomba = {}
animaciones_goomba["derecha"] = enemigo_goomba_der
animaciones_goomba["izquierda"] = enemigo_goomba_izq

animaciones_donkey = {}
animaciones_donkey["derecha" ] = enemigo_donkey_der
animaciones_donkey["izquierda" ] = enemigo_donkey_izq
animaciones_donkey["barril"] = enemigo_donkey_barril


class Enemy(pygame.sprite.Sprite):
    def __init__(self, tamaño,animacion,coordenadas,velocidad):
        super().__init__()
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.size = (self.ancho,self.alto)
        self.animaciones = animacion
        self.reescalar_animacion()
        self.image = self.animaciones["izquierda"][0]
        self.velocidad = velocidad
        self.vida = True
        self.dir = "izquierda"
        self.rect = self.image.get_rect()
        self.rect.x= coordenadas[0]
        self.rect.y= coordenadas[1]
        self.lados = obtener_rectangulos(self.rect)
        self.contador_pasos = 0
        self.clock = pygame.time.Clock()
        self.contador = 0
        self.tocando_piso = True
        self.gravedad = 1
        self.desplazamiento_y = 0

    def reescalar_animacion(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.size)

    def mover(self):
        
        for lado in self.lados:
            # if self.tocando_piso:
            self.lados[lado].x -= self.velocidad
            if self.lados[lado].x < 0:
                self.kill()

    
    def aplicar_gravedad(self,lista_plataformas):
        for plat in lista_plataformas:
            if self.lados['bottom'].colliderect(plat.lados["top"]):
                self.desplazamiento_y = 0
                self.tocando_piso = True
                self.lados['main'].bottom = plat.lados['main'].top + 5
                break
            else:
                self.tocando_piso = False

        if not self.tocando_piso:
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            self.desplazamiento_y += self.gravedad


    def animar(self,pantalla,rango, anima):
        animacion_enemigo = self.animaciones[anima]
        largo = len(animacion_enemigo) - rango
        
        if self.vida:
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(animacion_enemigo[self.contador_pasos], self.lados["main"])
            self.contador_pasos += 1

        elif not self.vida:
            largo = len(animacion_enemigo) - 1
            pantalla.blit(animacion_enemigo[largo], self.lados["main"])
            self.clock.tick(600)
            self.kill()   

    def draw_rect(self,pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, "Blue", self.lados[lado],3)

    def seguir_scroll(self,fondo,personaje):
        for lado in self.lados:
            if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                self.lados[lado].x -= 20
            elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":
                self.lados[lado].x += 20

    def encapsular(self,g_topes,velocidad):
        for tope in g_topes:
            if self.lados["main"].colliderect(tope.lados["right"]):
                self.dir = "derecha"
                self.velocidad = -velocidad
            elif self.lados["main"].colliderect(tope.lados["left"]):
                self.dir = "izquierda"
                self.velocidad = velocidad

    def update(self,pantalla,fondo,personaje,rango,g_plat):
        match self.dir:
            case "izquierda":
                self.animar(pantalla,rango, "izquierda")
            case "derecha":
                self.animar(pantalla,rango, "derecha")
        self.seguir_scroll(fondo,personaje)
        self.mover()
        self.aplicar_gravedad(g_plat)




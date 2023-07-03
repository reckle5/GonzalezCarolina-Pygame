from typing import Any
import pygame

from config import *

lista_colision_piso =[ (3312,700)]

caja_moneda = [pygame.image.load("./src/recursos/plataformas/1.png"),
            pygame.image.load("./src/recursos/plataformas/2.png"),
            pygame.image.load("./src/recursos/plataformas/3.png"),
            pygame.image.load("./src/recursos/plataformas/5.png"),
            ]

caja_ladrillo = [pygame.image.load("./src/recursos/plataformas/4.png")]

class Piso(pygame.sprite.Sprite):
    def __init__(self,personaje,fondo_width):
        super().__init__()

        self.image = pygame.Rect((0,700,fondo_width,40))
        self.rect = self.image
        self.rect.top = personaje.lados["main"].bottom  
        self.lados = obtener_rectangulos(self.rect)

    def draw_rect(self,pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, "Blue", self.lados[lado],3)
    



class Plataforma(pygame.sprite.Sprite):
    def __init__(self,tamaño,animacion,coordenadas):
        super().__init__()

        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.size = (self.ancho,self.alto)
        #animaciones
        self.animaciones = animacion
        self.image = self.animaciones[0]
        self.contador = 0
        self.reescalar_animaciones()
        #rectangulos
        self.rect = self.animaciones[0].get_rect()
        self.rect.x = coordenadas[0]    
        self.rect.y = coordenadas[1]
        self.lados = obtener_rectangulos(self.rect)
        self.golpeado = False

    def reescalar_animaciones(self):
        reescalar_imagenes(self.animaciones, self.size)

    def animar_plataforma(self,pantalla):
        animacion = self.animaciones
        largo = len(animacion) -1
        if not self.golpeado:
            if self.contador >= largo:
                self.contador = 0
            pantalla.blit(animacion[self.contador], self.lados["main"])
            self.contador += 1
        elif self.golpeado:
            pantalla.blit(animacion[3], self.lados["main"])


    def draw_rect(self,pantalla):
            for lado in self.lados:
                    pygame.draw.rect(pantalla, "Blue", self.lados[lado],3)

    def seguir_scroll(self,fondo,personaje):
            for lado in self.lados:
                if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                    self.lados[lado].x -= 20
                elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":
                    self.lados[lado].x += 20
                    

    def update(self,pantalla,fondo,personaje):
        self.seguir_scroll(fondo,personaje)
        self.animar_plataforma(pantalla)
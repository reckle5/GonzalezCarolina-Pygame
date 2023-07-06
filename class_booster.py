from typing import Any
import pygame
from funciones import *

hongo_rojo = pygame.image.load("./src/recursos/hongo_vida/0.png")
hongo_rojo = pygame.transform.scale(hongo_rojo,(50,50))


class Booster(pygame.sprite.Sprite):
    def __init__(self, imagen,coordenadas ):
        super().__init__()

        self.image = imagen
        #rects
        self.rect = self.image.get_rect()
        self.rect.x= coordenadas[0]
        self.rect.y= coordenadas[1]
        self.lados = obtener_rectangulos(self.rect)
        self.velocidad = 10
        self.gravedad = 18

    def mover(self):
        for lado in self.lados:
            self.lados[lado].x += self.velocidad
            # if self.lados[lado].x > :
            #     self.kill()

    def animar(self,pantalla):
        pantalla.blit(self.image, self.lados["main"])

    def draw_rect(self,pantalla):
        for lado in self.lados:
                pygame.draw.rect(pantalla, "Black", self.lados[lado],3)
    
    def seguir_scroll(self,fondo,personaje):
        for lado in self.lados:
            if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                self.lados[lado].x -= 20
            elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":
                self.lados[lado].x += 20
    
    def aplicar_gravedas(self):
        if self.lados["main"].y < 725:
            self.lados["main"].y += self.gravedad
    
    def update(self,pantalla,fondo,personaje):
        self.animar(pantalla)
        self.mover()
        self.aplicar_gravedas()
        self.seguir_scroll(fondo,personaje)
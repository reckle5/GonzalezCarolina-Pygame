import pygame
from config import *

modeda = [pygame.image.load("./src/recursos/coin/0.png"),
        pygame.image.load("./src/recursos/coin/1.png"),
        pygame.image.load("./src/recursos/coin/2.png"),
        pygame.image.load("./src/recursos/coin/3.png")
        ]

class Coin(pygame.sprite.Sprite):
    def __init__(self, tamaño,animacion,coordenadas ):
        super().__init__()
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.size = (self.ancho,self.alto)
        self.animaciones = animacion
        self.reescalar_animacion()
        self.image = self.animaciones[0]
        #rects
        self.rect = self.image.get_rect()
        self.rect.x= coordenadas[0]
        self.rect.y= coordenadas[1]
        self.lados = obtener_rectangulos(self.rect)
        self.contador = 0

    def reescalar_animacion(self):
            reescalar_imagenes(self.animaciones, self.size)
    
    def animar_moneda(self,pantalla):
        animacion_moneda = self.animaciones
        largo = len(animacion_moneda)
        
        if self.contador >= largo:
            self.contador = 0
        pantalla.blit(animacion_moneda[self.contador], self.lados["main"])
        self.contador += 1
    
    def draw_rect(self,pantalla):
        for lado in self.lados:
                pygame.draw.rect(pantalla, "Black", self.lados[lado],3)

    def seguir_scroll(self,fondo,personaje):
        for lado in self.lados:
            if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                self.lados[lado].x -= 20
            elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":
                self.lados[lado].x += 20

    def update(self,pantalla,fondo,personaje):
        self.animar_moneda(pantalla)
        self.seguir_scroll(fondo,personaje)

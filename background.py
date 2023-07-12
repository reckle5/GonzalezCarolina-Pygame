import pygame
from pygame.locals import *
from config import *

fondo_img = pygame.image.load("./src/recursos/rooms/level_1.png")
ancho_1 = fondo_img.get_width() * 3
alto_1 = fondo_img.get_height() * 4

fondo_2 = pygame.image.load("./src/recursos/nivel_2/room/0.png")

class Background():
    def __init__(self,fondo,width,tamaño):
        # super().__init__()
        self.image = fondo
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.image = pygame.transform.scale(self.image,(self.ancho, self.alto))
        self.start_scrolling = width // 2 - 100
        self.desplazamiento_derecha = False
        self.desplazamiento_izquierda = False

    def desplazamiento_x(self, compensar_x):
        copy_bg = self.image.copy()
        self.image.blit(copy_bg, (compensar_x, 0))
        if compensar_x < 0:
            self.image.blit(copy_bg, (self.ancho + compensar_x, 0), (0, 0, -compensar_x, self.alto))
        else:
            self.image.blit(copy_bg, (0, 0), (self.ancho - compensar_x, 0, compensar_x, self.alto))


import pygame
from pygame.sprite import _Group

barriles = [pygame.transform.scale(pygame.image.load("./src./recursos/nivel_2/barriles/1.png"),(60,30)),
        pygame.transform.scale(pygame.image.load("./src./recursos/nivel_2/barriles/2.png"),(60,30)),
        pygame.transform.scale(pygame.image.load("./src./recursos/nivel_2/barriles/0.png"),(60,30))]


class Barril(pygame.sprite.Sprite):
    def __init__(self,animacion,velocidad) :
        super().__init__()

        self.animaciones = animacion
        self.image = self.animaciones[0]
        self.velocidad = velocidad
        self.gravedad = 1

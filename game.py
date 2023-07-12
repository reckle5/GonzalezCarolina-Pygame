import pygame
from config import *
from class_estado_juego import *

class Game():
    def __init__(self):

        pygame.init()

        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
        self.caption = pygame.display.set_caption("Spidey Game")
        self.estado = EstadoJuego()

    def jugar(self):
        
        while True:
            self.estado.manejo_de_estado(self.pantalla)
            print(self.estado.personaje_juego.cooldown_proyectil)
            self.reloj.tick(FPS)

            pygame.display.flip()
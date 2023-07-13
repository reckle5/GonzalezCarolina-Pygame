import pygame
from pygame.locals import *
import random

#game
pygame.font.init()
WIDTH = 1800
HEIGHT = 900
CENTER = (WIDTH // 2, HEIGHT // 2)
AREA = WIDTH * HEIGHT
FPS = 20
tiempo_juego = 1

#PERSONAJE
tamaño_personaje = (70,120)
x_inicial = 450  
y_inicial = 750
coordenadas = (x_inicial,y_inicial) 

#enemigos
tamaño_goomba = (38,38)

#moneda
tamaño_moneda = (30,30)

#proyectil
tamaño_proyectil = (30,40)
velocidad_proyectil = 15

#font
font = pygame.font.Font("./src/recursos/game_font/PressStart2P-Regular.ttf", 15)
font_ranking = pygame.font.Font("./src/recursos/game_font/ARCADE_I.TTF", 25)
font_ranking_bold = pygame.font.Font("./src/recursos/game_font/ARCADE_N.TTF", 18)


#random color
color_base = "Grey"
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

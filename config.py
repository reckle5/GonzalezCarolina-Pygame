import pygame
from pygame.locals import *

from sprites_personaje import *
from personaje import *

WIDTH = 1800
HEIGHT = 900
CENTER = (WIDTH // 2, HEIGHT // 2)
AREA = WIDTH * HEIGHT
FPS = 20


LILA = (161,146,233)

#PERSONAJE
x_inicial = 300  
y_inicial = 820
coordenadas = (x_inicial,y_inicial)
posicion_actual_x = y_inicial 
contador_pasos = 0

#WEB
max_web = 40

# #GRAVEDAD
esta_saltando = False
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
desplazamiento_y = 0

def obtener_rectangulos(rect_principal)->dict:
    diccionario ={}
    diccionario['main'] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom-10, rect_principal.width,10)
    diccionario["right"] = pygame.Rect(rect_principal.right-2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width,10)
    return diccionario
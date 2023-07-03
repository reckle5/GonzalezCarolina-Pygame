import pygame
from pygame.locals import *
import random

WIDTH = 1800
HEIGHT = 900
CENTER = (WIDTH // 2, HEIGHT // 2)
AREA = WIDTH * HEIGHT
FPS = 20


#PERSONAJE
tamaño_personaje = (70,120)
x_inicial = 300  
y_inicial = 725
coordenadas = (x_inicial,y_inicial) 

#enemigos
tamaño_goomba = (38,38)

#moneda
tamaño_moneda = (30,30)

#proyectil
tamaño_proyectil = (30,40)
velocidad_proyectil = 15

def obtener_rectangulos(rect_principal)->dict:
    diccionario ={}
    diccionario['main'] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom-11, rect_principal.width,10)
    diccionario["right"] = pygame.Rect(rect_principal.right-2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width,10)
    return diccionario

def reescalar_imagenes(lista_animaciones,size):
    for i in range(len(lista_animaciones)): 
        lista_animaciones[i] = pygame.transform.scale(lista_animaciones[i], (size))

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada
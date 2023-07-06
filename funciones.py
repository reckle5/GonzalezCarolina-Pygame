import pygame

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


def agregar_a_grupo(lista_objetos,grupo):
    for i in lista_objetos:
        grupo.add(i)



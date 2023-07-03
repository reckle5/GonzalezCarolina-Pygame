import pygame
from config import *


enemigo_goomba = [pygame.image.load("./src/recursos/bichos/0.png"),
        pygame.image.load("./src/recursos/bichos/1.png"),
        pygame.image.load("./src/recursos/bichos/2.png")
        ]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, tamaño,animacion,coordenadas ):
        super().__init__()
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.size = (self.ancho,self.alto)
        self.animaciones = animacion
        self.reescalar_animacion()
        self.image = self.animaciones[0]
        self.velocidad = 10
        self.vida = True
        #rects
        self.rect = self.image.get_rect()
        self.rect.x= coordenadas[0]
        self.rect.y= coordenadas[1]
        self.lados = obtener_rectangulos(self.rect)
        self.contador_pasos = 0

    def reescalar_animacion(self):
            reescalar_imagenes(self.animaciones, self.size)

    def mover(self):
        for lado in self.lados:
            self.lados[lado].x -= self.velocidad
            if self.lados[lado].x < 0:
                self.kill()

    def animar(self,pantalla):
        self.vida = True
        animacion_enemigo = self.animaciones
        largo = len(animacion_enemigo) - 1 
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion_enemigo[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
        if not self.vida:
            pantalla.blit(animacion_enemigo[2], self.lados["main"])

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
        self.mover()
        self.animar(pantalla)
        # if self.fuera_de_pantalla:
        #     self.kill()







# goomba = [pygame.image.load("./src/recursos/bichos/0.png"),
#         pygame.image.load("./src/recursos/bichos/1.png"),
#         pygame.image.load("./src/recursos/bichos/2.png")
#         ]

# lista_enemies = [goomba]

# lista_enemies = reescalar_imagenes(lista_enemies, (110,140))

# # enemies.add(goomba)
# class BadGuys(pygame.sprite.Sprite):
#     def __init__(self, image_path,center, speed):
#         super().__init__()

#         self.image =  image_path
#         self.rect = self.image[0].get_rect()
#         self.rect.center = center
#         self.speed = speed
#         # self.aceleration = 1.2

#     # def mover_personaje_derecha(self,lados):
#     #     for lado in lados:
#     #         lados[lado].x += self.speed_x
#     #     return
    
#     # def mover_personaje_izquierda(self,lados):
#     #     for lado in lados:
#     #         lados[lado].x -= self.speed_x
#     #     return

#     def update(self):
#         # self.aceleration += 0.1
#         self.rect.y += self.speed

import pygame
from config import *
import os

speed = 10
speed_enemies = 10
max_enemies = 10
size_enemies = (40,40)

goomba = [pygame.image.load(os.path.join("src/recursos/bichos","0.png")),
        pygame.image.load(os.path.join("src/recursos/bichos","1.png")),
        ]

def rescalar_img(lista):
    lista_resc = []
    for i in lista:
        img_resc = pygame.transform.scale(i, (40,35))
        lista_resc.append(img_resc)
    return lista_resc


goomba = rescalar_img(goomba)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__() 
        self.image = goomba[0] 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step_index = 0
        self.hitbox = (self.rect.x, self.rect.y, 64, 64)


    def step(self):
        if self.step_index >= 2:
            self.step_index = 0

    def off_screen(self):
        return not (self.rect.x - self.rect.width )

    def update(self):
        # self.hitbox = (self.rect.x -10, self.rect.y , 40, 40)
        # pygame.draw.rect(screen, (0, 0, 0), self.hitbox, 3)
        self.rect.x -= 15
        self.step()
        self.image = goomba[self.step_index]
        self.step_index += 1
        if self.rect.x < 0:
            self.kill()
    
    def draw_hitbox(self,screen):
        self.hitbox = (self.rect.x -10, self.rect.y , 40, 40)
        pygame.draw.rect(screen, (0, 0, 0), self.hitbox, 3)
    
    






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

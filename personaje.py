import pygame
from config import *

def reescalar_imagenes(lista_animaciones,size):
    for lista in lista_animaciones:
        for i in range(len(lista)): 
            lista[i] = pygame.transform.scale(lista[i], (size))
    return lista_animaciones

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada

class Spidey(pygame.sprite.Sprite):
    def __init__(self,coordenada,lista_animacion,posicion_actual_x):
        super().__init__()

        self.walk = lista_animacion
        self.image = self.walk
        self.rect = self.image[0].get_rect()
        self.rect.midbottom = coordenada
        self.contador_pasos = 0
        self.posicion = posicion_actual_x
        self.speed_x = 10
        self.speed_y = 0
        self.jump_count = 0
        self.webs = []
        self.left = False
        self.right = True
        self.cool_down_count = 0

    def mover_personaje_derecha(self,lados):
        self.right = True
        self.left = False
        for lado in lados:
            lados[lado].x += self.speed_x
        return
    def mover_personaje_izquierda(self,lados):
        not self.left,self.right
        for lado in lados:
            lados[lado].x -= self.speed_x
        return
    
    def animar_personaje(self, pantalla, animacion):
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.rect)
        self.contador_pasos += 1 
        return
    
    def animar_una_vez(self,pantalla,animacion):
        largo = len(animacion)
        if self.contador_pasos < largo-1:
            self.contador_pasos += 1
        pantalla.blit(animacion[self.contador_pasos], self.rect)
        return
    
    def direction(self):
        if self.right:
            return 1
        elif self.left:
            return -1
        
    def cooldown(self):
        if self.cool_down_count == 4:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def ataque(self,telaraña,enemies,screen):
        self.hit_collision(enemies)
        self.cooldown()
        if self.cool_down_count == 0:
            web = telaraña
            # web = Web(personaje_telaraña, self.rect.x, self.rect.y, self.direction())
            self.webs.append(web)
            self.cool_down_count = 1
            for web in self.webs:   
                web.move()
                web.update(screen)
                if web.off_screen(1500):
                    self.webs.remove(web)
        print(len(self.webs))
        print(self.cool_down_count)
    
    def hit_collision(self,enemies):
        for enemy in enemies:
            for web in self.webs:
                if enemy.hitbox[0] < web.rect.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < web.rect.y < enemy.hitbox[1] + enemy.hitbox[3]:
                    print("player hit enemy")




class Web(pygame.sprite.Sprite):
    def __init__(self, personaje_telaraña,x,y,direction):
        super().__init__()

        self.image = personaje_telaraña
        self.rect = self.image.get_rect()
        self.rect.x = x + 32
        self.rect.y = y + 40
        self.direction = direction
        self.hitbox = (self.rect.x, self.rect.y, 64, 64)

    def move(self):
        if self.direction == 1:
            self.rect.x += 10
            print(self.rect.x)
        elif self.direction == -1:
            self.rect.x -= 10
    
    def off_screen(self,width):
        return not(self.rect.x >= 0 and self.rect.x <= width)
    
    def update(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def draw_hitbox(self,screen):
        self.hitbox = (self.rect.x -7, self.rect.y +15, 35, 35)
        pygame.draw.rect(screen, (0, 0, 0), self.hitbox, 3)



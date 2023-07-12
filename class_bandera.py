import pygame
from config import *
from funciones import *

palo_bandera = pygame.image.load("./src./recursos/bandera/0.png")
palo_bandera = pygame.transform.scale(palo_bandera, (30,568))
bola_palo = pygame.image.load("./src./recursos/bandera/1.png")
bola_palo = pygame.transform.scale(bola_palo, (35,35))
palo_rect = palo_bandera.get_rect()
bola_rect = bola_palo.get_rect()

flag = [ pygame.transform.scale(pygame.image.load("./src./recursos/bandera/2.png"),(60,30)),
        pygame.transform.scale(pygame.image.load("./src./recursos/bandera/3.png"),(60,30)),
        pygame.transform.scale(pygame.image.load("./src./recursos/bandera/4.png"),(60,30)),
        palo_bandera,
        bola_palo
        ]


class Bandera(pygame.sprite.Sprite):
    def __init__(self, animacion,pos,bola_rect,palo_rect):
        super().__init__()

        self.animaciones = animacion
        self.image = self.animaciones[0]
        self.rect = self.image.get_rect()
        self.bola = self.animaciones[4]
        self.bola_rect = bola_rect
        self.bola_rect.x = 9505
        self.bola_rect.y = 140
        self.palo = self.animaciones[3]
        self.palo_rect = palo_rect
        self.palo_rect.x = 9510
        self.palo_rect.y = 170
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.lados = obtener_rectangulos(self.rect)
        self.lados_bola = obtener_rectangulos(self.bola_rect)
        self.lados_palo = obtener_rectangulos(self.palo_rect)
        self.contador = 0
        self.bandera_tocada = False
        self.gravedad = 15

        
    def animar_bandera(self,pantalla):
        animacion_bandera = self.animaciones
        largo = len(animacion_bandera)-2
        
        if self.contador >= largo:
            self.contador = 0
        pantalla.blit(self.palo, (self.palo_rect.x,self.palo_rect.y))
        pantalla.blit(self.bola, (self.bola_rect.x,self.bola_rect.y))
        pantalla.blit(animacion_bandera[self.contador], self.lados["main"])
        self.contador += 1


    def colision(self, g_jugador,plat):
            if self.lados["main"].colliderect(g_jugador.lados["main"]):
                # Bandera_tocada = True
                self.lados["main"].y += self.gravedad
                if self.lados["main"].y == 720:
                    self.lados["main"].bottom = plat.lados["main"].top


    def draw_rect(self,pantalla):
        for lado in self.lados:
                pygame.draw.rect(pantalla, "Black", self.lados[lado],3)

    def seguir_scroll(self,fondo,personaje):
        for lado in self.lados_bola:
            if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                self.lados_bola[lado].x -= 20
            elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":
                self.lados_bola[lado].x += 20
        for lado in self.lados_palo:
            if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                self.lados_palo[lado].x -= 20
            elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":    
                self.lados_palo[lado].x += 20
        for lado in self.lados:
            if fondo.desplazamiento_derecha and personaje.que_hace == "derecha":
                self.lados[lado].x -= 20
            elif fondo.desplazamiento_izquierda and personaje.que_hace == "izquierda":    
                self.lados[lado].x += 20

    def update(self, g_jugador,fondo,pantalla,plat):
        self.animar_bandera(pantalla)
        self.colision( g_jugador,plat)
        self.seguir_scroll(fondo,g_jugador)
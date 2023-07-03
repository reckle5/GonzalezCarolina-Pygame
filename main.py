import pygame
import sys
from config import *
from personaje import *
from pygame.locals import *
from sprites_personaje import *
from modo import *
from background import *
from mushroom_generator import *
from class_plataforma import *

pygame.init()

RELOJ = pygame.time.Clock() 
pantalla_juego = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spidey Game")

mi_spiderman = Spidey(tamaño_personaje,dic_animaciones,coordenadas,15)
# proyectil_telaraña = Telaraña((30,40), 10, personaje_telaraña,(mi_spiderman.lados["main"].x,mi_spiderman.lados["main"].y),1)

fondo_juego = Background(fondo_img, WIDTH)

piso = Piso(mi_spiderman,1500)
# coli = Piso(mi_spiderman,3312,fondo_juego.ancho)

plataforma_caja1 = Plataforma((50,50), caja_moneda, (700, 620))
plataforma_caja2 = Plataforma((50,50), caja_moneda, (800, 620))
# plataforma_caja3 = Plataforma((50,50), caja_moneda, (1800, 630))
# plataforma_caja4 = Plataforma((50,50), caja_moneda, (2100, 630))
# plataforma_caja5 = Plataforma((50,50), caja_moneda, (2500, 630))
plataforma_ladrillo = Plataforma((50,50),caja_ladrillo,(750,620))



# goomba = Enemy(tamaño_goomba, enemigo_goomba, coordenadas_enemigo)

# lista_plataformas = [lados_piso]
teclas_presionadas = {}

player_group = pygame.sprite.Group()
player_group.add(mi_spiderman) 

proyectil_group = pygame.sprite.Group()
enemigos_group = pygame.sprite.Group()
plataformas_group = pygame.sprite.Group()
plataformas_sorpresa_group = pygame.sprite.Group()
all_plataformas = pygame.sprite.Group()
moneda_group = pygame.sprite.Group()
plataformas_sorpresa_group.add(plataforma_caja1)
plataformas_sorpresa_group.add(plataforma_caja2)
plataformas_group.add(plataforma_ladrillo)
# plataformas_group.add(plataforma_caja4)
# plataformas_group.add(plataforma_caja5)
plataformas_group.add(piso)
all_plataformas.add(plataformas_sorpresa_group)
all_plataformas.add(plataformas_group)


def actualizar_pantalla(pantalla,fondo_img,lista_plataformas,g_plataformas_sorpresa,g_plataformas_ordinarias):
    pantalla.blit(fondo_img, (0,0))
    mi_spiderman.update(pantalla,enemigos_group,lista_plataformas,g_plataformas_sorpresa,g_plataformas_ordinarias,moneda_group)
    all_plataformas.update(pantalla,fondo_juego,mi_spiderman)
    proyectil_group.draw(pantalla)
    moneda_group.update(pantalla,fondo_juego,mi_spiderman)


def generar_enemigos(g_enemigos,cantidad):
    if len(g_enemigos) == 0:
        for i in range(cantidad):
            x = random.randrange(2500, 1689, -1)
            enemigo = Enemy(tamaño_goomba, enemigo_goomba, (x,760))
            g_enemigos.add(enemigo)
            
while True:
    
    RELOJ.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            # Registrar la tecla presionada en el diccionario
            teclas_presionadas[evento.key] = True           
        elif evento.type == pygame.KEYUP:
            # Eliminar la tecla del diccionario cuando se deja de presionar
            if evento.key in teclas_presionadas:
                del teclas_presionadas[evento.key]
    # print(fondo_juego.ancho)
    # print(mi_spiderman.rect.x)
    if pygame.K_TAB in teclas_presionadas: 
        cambiar_modo()
    elif pygame.K_RIGHT in teclas_presionadas:  
        if mi_spiderman.lados["main"].x < WIDTH - mi_spiderman.velocidad - mi_spiderman.lados["main"].x:
            mi_spiderman.que_hace = "derecha"
        else:
            mi_spiderman.velocidad = 0
            mi_spiderman.que_hace = "derecha"
        if mi_spiderman.lados["main"].x > fondo_juego.start_scrolling: 
            fondo_juego.desplazamiento_derecha = True       
            fondo_juego.desplazamiento_izquierda = False
            fondo_juego.desplazamiento_x(-20)            
    elif pygame.K_LEFT in teclas_presionadas: 
        if mi_spiderman.lados["main"].x < WIDTH - mi_spiderman.velocidad - mi_spiderman.lados["main"].x: 
            mi_spiderman.que_hace = "izquierda"
        else:
            mi_spiderman.velocidad = 0
            mi_spiderman.que_hace = "izquierda"
        if mi_spiderman.lados["main"].x > fondo_juego.start_scrolling:
            fondo_juego.desplazamiento_derecha = False
            fondo_juego.desplazamiento_izquierda = True
            fondo_juego.desplazamiento_x(20)
    elif pygame.K_UP in teclas_presionadas: 
            mi_spiderman.que_hace = "salta" 
            print(mi_spiderman.saltos_actuales)
    elif pygame.K_DOWN in teclas_presionadas: 
        mi_spiderman.que_hace = "defensa"
    elif pygame.K_SPACE in teclas_presionadas: 
        mi_spiderman.que_hace = "dispara"   
        proyectil_group.add(mi_spiderman.crear_proyectil())
        mi_spiderman.cooldown_proyectil = 100
    else:
        mi_spiderman.que_hace = "quieto"

    actualizar_pantalla(pantalla_juego,fondo_juego.image,all_plataformas,plataformas_sorpresa_group,plataformas_group)
    generar_enemigos(enemigos_group,2)
    proyectil_group.draw(pantalla_juego)
    enemigos_group.update(pantalla_juego,fondo_juego,mi_spiderman)
    proyectil_group.update(velocidad_proyectil,proyectil_group,enemigos_group)

    if get_mode() == True:
        for lado in mi_spiderman.lados:
            pygame.draw.rect(pantalla_juego, "Orange", mi_spiderman.lados[lado], 3)
        
        for enemigo in enemigos_group:
            enemigo.draw_rect(pantalla_juego)
        
        
        for plataformas in all_plataformas:
            plataformas.draw_rect(pantalla_juego)

        # coli.draw_rect(pantalla_juego,"Black")



    pygame.display.flip()









import pygame 
import sys
from config import *
from personaje import *
from pygame.locals import *
from sprites_personaje import *
from modo import *
from background import *
from mushroom_generator import *
import random


pygame.init()

reloj = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spidey Game")

sprites = pygame.sprite.Group()
baddies  = pygame.sprite.Group()

player = Spidey(coordenadas,personaje_camina,posicion_actual_x)
bg = pygame.image.load("./src/recursos/rooms/level_1.png").convert()

backg = Background(bg, WIDTH, player)

web = Web(personaje_telaraña, player.rect.x, player.rect.y, player.direction())


lados_floor = obtener_rectangulos(backg.floor)
lados_floor2 = obtener_rectangulos(backg.floor2)

lados_personajes = obtener_rectangulos(player.rect)

lista_plataformas = [lados_floor,lados_floor2]
accion = "quieto"

teclas_presionadas = {}


def aplicar_gravedad(pantalla, animacion,plataformas,lados_personajes):
    global desplazamiento_y
    global esta_saltando
    if esta_saltando:
        player.animar_personaje(pantalla,animacion)
        for lado in lados_personajes:
            lados_personajes[lado].y += desplazamiento_y
        if (desplazamiento_y + gravedad) < limite_velocidad_caida:
            desplazamiento_y += gravedad
    for piso in plataformas:
        if lados_personajes['bottom'].colliderect(piso['top']):
            desplazamiento_y = 0
            esta_saltando = False
            lados_personajes['main'].bottom = piso['main'].top
            break
        else:
            esta_saltando = True
    return

def actualizar_pantalla(pantalla, accion, plataformas,lados_personaje):
    global esta_saltando
    global desplazamiento_y,fps

    match accion:
        case "caminar derecha":
            if not esta_saltando:
                player.animar_personaje(pantalla,personaje_camina)
            player.mover_personaje_derecha(lados_personaje)
        case "caminar izquierda":
            if not esta_saltando: 
                player.animar_personaje(pantalla,personaje_camina_izquierda)
            player.mover_personaje_izquierda(lados_personajes)
            player.posicion -= 1
        case "saltar":  
            esta_saltando = True
            desplazamiento_y = potencia_salto
        case "defensa" :
            if not esta_saltando: 
                player.animar_una_vez(pantalla, personaje_defensa)  
        case "ataque" :
            if not esta_saltando:
                player.animar_personaje(pantalla,personaje_ataque)
                player.ataque(web,baddies,pantalla)
                web.update(pantalla)

                
                
        case "quieto": 
            if not esta_saltando:
                player.animar_personaje(pantalla, personaje_quieto)
    aplicar_gravedad(pantalla, personaje_salta, plataformas, lados_personajes)


def generate_enemies(count):
    if len(baddies) == 0:
        for i in range(count):
            x = random.randrange(2000, 1689, -1)
            enemy = Enemy(x, 760)
            # enemy.update(display)
            baddies.add(enemy)           

while True:
    
    reloj.tick(FPS)
    current_time = pygame.time.get_ticks()

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
            
    if pygame.K_TAB in teclas_presionadas: 
        cambiar_modo()
    elif pygame.K_RIGHT in teclas_presionadas:  
        accion = "caminar derecha"
        if player.posicion < stage_width:
            print(stage_width)
            print(player.posicion)  
            player.posicion += player.speed_x
        if player.posicion > backg.start_scrolling:
            backg.scrollX(-20)
    elif pygame.K_LEFT in teclas_presionadas:
        accion = "caminar izquierda"
        if player.posicion > 0:
            player.posicion -= player.speed_x
        if player.posicion < backg.start_scrolling:
            backg.scrollX(20)
    elif pygame.K_UP in teclas_presionadas: 
        accion = "saltar" 
    elif pygame.K_DOWN in teclas_presionadas: 
        accion = "defensa"
    elif pygame.K_SPACE in teclas_presionadas: 
        accion = "ataque"
    else:
        accion = "quieto"


    display.blit(backg.image,(0,0))

    actualizar_pantalla(display,accion,lista_plataformas,lados_personajes)
    

    generate_enemies(1)


    baddies.update()
    baddies.draw(display)
    
    if get_mode() == True:
        for lado in lados_personajes:
            pygame.draw.rect(display, "Orange", lados_personajes[lado], 3)
            pygame.display.update()
        
        for plat in lista_plataformas:
            for lado in plat:
                pygame.draw.rect(display, "Blue", plat[lado],3)
        
        for i in baddies:
            i.draw_hitbox(display)
        
        web.draw_hitbox(display) 

    pygame.display.flip()


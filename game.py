import pygame,sys,time,csv
from config import *
from background import *
from class_plataforma import *
from personaje import *
from class_moneda import*
from funciones import *
from boton_seleccionar import *
from claas_enemigos import *
from sprites_personaje import *
from pygame.locals import *



class Game:
    def __init__(self):

        pygame.init()

        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
        self.caption = pygame.display.set_caption("Spidey Game")
        self.fondo_imagen = pygame.image.load("./src/recursos/rooms/level_1.png")
        self.in_game = False
        self.is_running = False
        self.is_game_over = False
        self.tiempo_m = pygame.time.get_ticks()
        self.tiempo_s = int(self.tiempo_m /1000)
        self.teclas_presionadas = {}
        self.debug = False
        self.puntajes_juego = None
        #### SPRITES
        self.sprites = pygame.sprite.Group()
        #GRUPO PERSONAJE
        self.player_group = pygame.sprite.Group()
        self.proyectil_group = pygame.sprite.Group()
        self.personaje_juego =  Spidey(tamaño_personaje,dic_animaciones,coordenadas,15)
        self.player_group.add(self.personaje_juego)
        #GRUPO ENEMIGOS
        self.goomba_group = pygame.sprite.Group()
        self.tortuga_group = pygame.sprite.Group()
        self.tortuga = Enemy((50,50),animaciones_tortuga,(4000, 250),10)
        self.tortuga_group.add(self.tortuga)
        self.all_enemies = pygame.sprite.Group()
        self.all_enemies.add(self.goomba_group)
        self.all_enemies.add(self.tortuga_group)
        #GRUPO PLATAFORMAS
        self.plataformas_group = pygame.sprite.Group()
        self.plataformas_sorpresa_group = pygame.sprite.Group()
        self.all_plataformas = pygame.sprite.Group()
        self.plataforma_boost =  pygame.sprite.Group()
        #GRUPO OBJETOS INTERACTIVOS
        self.moneda_group = pygame.sprite.Group()
        #BOOSTER =
        self.plataforma_booster_group = pygame.sprite.Group()
        self.hongo_boost = pygame.sprite.Group()
        #FONDO
        self.fondo = Background(fondo_img, WIDTH)
        #PLATAFORMA PISO
        self.piso_1 = Piso(self.personaje_juego,0,700,3310,40)
        self.piso_2 = Piso(self.personaje_juego,3405,700,730,40)
        self.piso_3 = Piso(self.personaje_juego,4280,700,3070,40)
        self.piso_4 = Piso(self.personaje_juego,7450,700,4000,40)
        #PLATAFORMA TUBOS
        self.tubo_1 = Generar_rects(1350,670,85,130)
        self.tubo_2 = Generar_rects(1830,610,85,190)
        self.tubo_3 = Generar_rects(2210,550,85,250)
        self.tubo_4 = Generar_rects(2740,550,85,250)
        # tope
        self.tope1 = Generar_rects(3750,220,10,100)
        self.tope2 = Generar_rects(4045,220,10,100)

        #MONEDAS
        self.moneda_group.add(self.personaje_juego.crear_moneda((1315,500)))
        self.moneda_group.add(self.personaje_juego.crear_moneda((1365,450)))
        self.moneda_group.add(self.personaje_juego.crear_moneda((1415,500)))
        self.coin_score = Coin((25,25),moneda,(910,10))
        #PLATAFORMAS ?
        self.plataforma_caja1 = Plataforma((50,50), caja_moneda, (700, 620),False)
        self.plataforma_caja2 = Plataforma((50,50), caja_moneda, (800, 620),False)

        self.plataforma_caja3 = Plataforma((50,50), caja_moneda, (850, 390),False)

        self.plataforma_caja4 = Plataforma((50,50), caja_moneda, (1890, 230),True) #caja invisible

        self.plataforma_caja5 = Plataforma((50,50), caja_moneda, (2450, 300),False)
        self.plataforma_caja6 = Plataforma((50,50), caja_moneda, (2400, 300),False)

        self.plataforma_caja7 = Plataforma((50,50), caja_moneda, (3550, 500),False)

        
        self.plataforma_caja8 = Plataforma((50,50), caja_moneda, (4300, 300),False) #boost


        #PLATAFORMAS LADRILLO
        self.plataforma_ladrillo = Plataforma((50,50),caja_ladrillo,(750,620),False)

        self.plataforma_ladrillo1 = Plataforma((50,50),caja_ladrillo,(800,390),False)
        self.plataforma_ladrillo2 = Plataforma((50,50),caja_ladrillo,(900,390),False)

        self.plataforma_ladrillo3 = Plataforma((50,50),caja_ladrillo,(2300, 300),False)
        self.plataforma_ladrillo4 = Plataforma((50,50),caja_ladrillo,(2350, 300),False)
        self.plataforma_ladrillo5 = Plataforma((50,50),caja_ladrillo,(2500, 300),False)
        self.plataforma_ladrillo6= Plataforma((50,50),caja_ladrillo,(2550, 300),False)

        self.plataforma_ladrillo7 = Plataforma((50,50),caja_ladrillo,(3750, 300),False)
        self.plataforma_ladrillo8 = Plataforma((50,50),caja_ladrillo,(3800, 300),False)
        self.plataforma_ladrillo9 = Plataforma((50,50),caja_ladrillo,(3850, 300),False)
        self.plataforma_ladrillo10 = Plataforma((50,50),caja_ladrillo,(3900, 300),False)
        self.plataforma_ladrillo11 = Plataforma((50,50),caja_ladrillo,(3950, 300),False)
        self.plataforma_ladrillo12 = Plataforma((50,50),caja_ladrillo,(4000, 300),False)
        self.plataforma_ladrillo13 = Plataforma((50,50),caja_ladrillo,(4200, 300),False)
        self.plataforma_ladrillo14 = Plataforma((50,50),caja_ladrillo,(4250, 300),False)

        self.plataforma_ladrillo15 = Plataforma((50,50),caja_ladrillo,(3500, 500),False)
        self.plataforma_ladrillo16 = Plataforma((50,50),caja_ladrillo,(3600, 500),False)

        self.plataforma_ladrillo17 = Plataforma((50,50),caja_ladrillo,(4300, 500),False)

        self.lista_plat_sorpresa = [self.plataforma_caja1,
                                    self.plataforma_caja2,
                                    self.plataforma_caja3,
                                    self.plataforma_caja4,
                                    self.plataforma_caja5,
                                    self.plataforma_caja6,
                                    self.plataforma_caja7
                                    ]
        self.lista_plat_ladrillo =[self.plataforma_ladrillo,
                                    self.plataforma_ladrillo1,
                                    self.plataforma_ladrillo2,
                                    self.plataforma_ladrillo3,
                                    self.plataforma_ladrillo4,
                                    self.plataforma_ladrillo5,
                                    self.plataforma_ladrillo6,
                                    self.plataforma_ladrillo7,
                                    self.plataforma_ladrillo8,
                                    self.plataforma_ladrillo9,
                                    self.plataforma_ladrillo10,
                                    self.plataforma_ladrillo11,
                                    self.plataforma_ladrillo12,
                                    self.plataforma_ladrillo13,
                                    self.plataforma_ladrillo14,
                                    self.plataforma_ladrillo15,
                                    self.plataforma_ladrillo16,
                                    self.plataforma_ladrillo17,

                                    self.piso_1,
                                    self.piso_2,
                                    self.piso_3,
                                    self.piso_4,
                                    self.tubo_1,
                                    self.tubo_2,
                                    self.tubo_3,
                                    self.tubo_4,
                                    ]
        self.topes = [self.tope1,
                    self.tope2]
        agregar_a_grupo(self.lista_plat_sorpresa,self.plataformas_sorpresa_group)
        agregar_a_grupo(self.lista_plat_ladrillo,self.plataformas_group) 
        self.plataforma_booster_group.add(self.plataforma_caja8)
        self.all_plataformas.add(self.plataformas_sorpresa_group)
        self.all_plataformas.add(self.plataformas_group)
        self.all_plataformas.add(self.topes)
        self.all_plataformas.add(self.plataforma_booster_group)
        self.sprites.add(self.player_group)
        self.sprites.add(self.proyectil_group)
        self.sprites.add(self.all_enemies)
        self.sprites.add(self.all_plataformas)
        self.sprites.add(self.moneda_group)
        self.sprites.add(self.plataforma_boost)
        self.sprites.add(self.hongo_boost)


    def main_menu(self):
        fondo = pygame.surface.Surface((1800,900))
        fondo.fill("Black")
        self.pantalla.blit(fondo, (0,0))
        flag = True
        pygame.display.set_caption("Menu")

        while flag:
            
            self.pantalla.blit(menu,(550,200))
            pos = pygame.mouse.get_pos()
            
            color_base = "Grey"
            boton_inicio = Boton("START GAME", color_base, "White",800, 460, 160,30)
            boton_salir = Boton("QUIT",color_base, "White",800, 520, 100,30)

            for b in [boton_inicio,boton_salir]:
                b.seleccionar_texto(pos)
                if b.spidey_visible:
                    print(b.spidey_visible)
                    self.pantalla.blit(select_spidey, (b.rect.x - 50, b.rect.y - 15))
                self.pantalla.blit(b.text, b.rect)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_inicio.draw(pos):
                        flag = False
                    if boton_salir.draw(pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def restart_game(self):
        flag = True
        pygame.display.set_caption("Game over - Menu")
        while flag:
        
            pos = pygame.mouse.get_pos()
            
            color_base = "Grey"
            boton_return = Boton("RESTART GAME",color_base, "White",800, 520, 60,20)
            boton_salir = Boton("QUIT",color_base, "White",800, 570, 60,20)

            for b in [boton_return,boton_salir]:
                b.seleccionar_texto(pos)
                if b.spidey_visible:
                    print(b.spidey_visible)
                    self.pantalla.blit(select_spidey, (b.rect.x - 50, b.rect.y - 15))
                self.pantalla.blit(b.text, b.rect)
            if boton_return.seleccionar_texto(pos):
                self.pantalla.blit(boton_return.text, boton_return.rect)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_return.draw(pos):
                        self.main_menu()
                        flag = False
                    if boton_salir.draw(pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def jugar(self):
        self.main_menu()

        self.in_game = True
        self.is_running = True
        self.is_game_over = False

        while self.in_game:
            self.reloj.tick(FPS)
            self.handler_events()
            self.update()
            self.render()
        
        self.pantalla_game_over()
        self.restart_game()


    def handler_events(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                # Registrar la tecla presionada en el diccionario
                    self.teclas_presionadas[evento.key] = True           
            elif evento.type == pygame.KEYUP:   
                # Eliminar la tecla del diccionario cuando se deja de presionar
                if evento.key in self.teclas_presionadas:
                    del self.teclas_presionadas[evento.key]

        if pygame.K_TAB in self.teclas_presionadas: 
            self.cambiar_modo()
        elif pygame.K_RIGHT in self.teclas_presionadas:  
            if self.personaje_juego.lados["main"].x < WIDTH - self.personaje_juego.velocidad - self.personaje_juego.lados["main"].x:
                self.personaje_juego.que_hace = "derecha"
            else:
                self.personaje_juego.velocidad = 0
                self.personaje_juego.que_hace = "derecha"
            if self.personaje_juego.lados["main"].x > self.fondo.start_scrolling: 
                self.fondo.desplazamiento_derecha = True       
                self.fondo.desplazamiento_izquierda = False
                self.fondo.desplazamiento_x(-20)            
        elif pygame.K_LEFT in self.teclas_presionadas: 
            if self.personaje_juego.lados["main"].x < WIDTH - self.personaje_juego.velocidad - self.personaje_juego.lados["main"].x: 
                self.personaje_juego.que_hace = "izquierda"
            else:
                self.personaje_juego.velocidad = 0
                self.personaje_juego.que_hace = "izquierda"
            if self.personaje_juego.lados["main"].x > self.fondo.start_scrolling:
                self.fondo.desplazamiento_derecha = False
                self.fondo.desplazamiento_izquierda = True
                self.fondo.desplazamiento_x(20)
        elif pygame.K_UP in self.teclas_presionadas: 
                self.personaje_juego.que_hace = "salta" 
        elif pygame.K_DOWN in self.teclas_presionadas: 
            self.personaje_juego.que_hace = "defensa"
        elif pygame.K_SPACE in self.teclas_presionadas and self.personaje_juego.cooldown_proyectil == 0: 
            self.personaje_juego.que_hace = "dispara"   
            self.personaje_juego.cooldown_proyectil = 2
            self.proyectil_group.add(self.personaje_juego.crear_proyectil()) 
        else:
            self.personaje_juego.que_hace = "quieto"
        
    def update(self):
        self.pantalla.blit(self.fondo.image, (0,0))
        self.personaje_juego.update(self.pantalla,self.goomba_group,self.all_plataformas,self.plataformas_sorpresa_group,self.plataformas_group,self.moneda_group,self.plataforma_booster_group,self.hongo_boost)
        self.all_plataformas.update(self.pantalla,self.fondo,self.personaje_juego)
        self.moneda_group.update(self.pantalla,self.fondo,self.personaje_juego)
        self.proyectil_group.update(velocidad_proyectil,self.proyectil_group,self.goomba_group,self.personaje_juego)
        self.coin_score.animar_moneda(self.pantalla)
        self.proyectil_group.draw(self.pantalla)
        self.hongo_boost.update(self.pantalla,self.fondo,self.personaje_juego)

        self.cronometo()
        self.generar_enemigos(1)
        self.tortuga.encapsular(self.topes,8)
        self.goomba_group.update(self.pantalla,self.fondo,self.personaje_juego,2)
        self.tortuga_group.update(self.pantalla,self.fondo,self.personaje_juego,2)

        print(self.personaje_juego.vida_actual)
        if self.debug == True:

            for lado in self.personaje_juego.lados:
                pygame.draw.rect(self.pantalla, "Orange", self.personaje_juego.lados[lado], 3)

            for enemigo in self.all_enemies:
                enemigo.draw_rect(self.pantalla)
            
            for plataformas in self.all_plataformas:
                plataformas.draw_rect(self.pantalla,(r,g,b))

    def render(self):
        if self.game_over():
            print("entreeee")
            self.pantalla_game_over()
        elif self.in_game:
            pygame.display.flip()

    def generar_enemigos(self,cantidad):
        if len(self.goomba_group) == 0:
            for i in range(cantidad):
                x = random.randrange(2500, 1089, -1)
                enemigo = Enemy(tamaño_goomba, animaciones_goomba, (x,760),10)
                self.goomba_group.add(enemigo)
                self.sprites.add(enemigo)

    def cambiar_modo(self):
        self.debug = not self.debug
    
    def cronometo(self):
        if self.tiempo_s  == self.tiempo_m:
            self.tiempo_s += 1
        minutos = int(self.tiempo_m/ 60) % 60
        segundos = self.tiempo_m % 60
        crono = f"{minutos:02}:{segundos:02}"
        tiempo = font.render(crono, True, "White")
        self.pantalla.blit(tiempo,(1172,20))

    def parar_elementos(self):
        for sprite in self.sprites:
            sprite.stop()

    def game_over(self):
        if self.personaje_juego.target_vida == 0 or self.personaje_juego.lados["main"].y > HEIGHT:
            self.personaje_juego.puntaje_anterior = self.personaje_juego.puntaje
            if self.personaje_juego.puntaje > self.personaje_juego.puntaje_mas_alto:
                self.personaje_juego.puntaje_mas_alto = self.personaje_juego.puntaje
            score = self.ranking()
            self.guardar_puntaje("scores.csv",score)
            self.puntajes_juego = self.leer_csv("scores.csv")
            self.personaje_juego.puntaje = 0
            self.is_game_over = True
            self.in_game = False
    
    def pantalla_game_over(self):
        fondo = pygame.surface.Surface((1800,900))
        fondo.fill("Black")
        msj = font.render("GAME OVER", True, "White")
        self.pantalla.blit(fondo, (0,0))
        self.pantalla.blit(msj, (800,450))
        self.draw_ranking()
        pygame.display.update()
        # pygame.display.flip()
        # self.restart_game
        self.is_game_over = False

    def ranking(self):
        dic_ranking = {}
        dic_ranking["puntaje"] = self.personaje_juego.puntaje
        dic_ranking["puntaje anterior"] = self.personaje_juego.puntaje_anterior
        dic_ranking["puntaje mas alto"] = self.personaje_juego.puntaje_mas_alto
        return [dic_ranking]

    def guardar_puntaje(self, archivo_csv, puntaje):
        with open(archivo_csv, "a", newline="") as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(puntaje)  
        print("Archivo creado")

    def leer_csv(self, nombre_archivo):
        puntajes = []
        with open(nombre_archivo, "r") as file:
            reader = csv.reader(file)
            for linea in reader:
                puntajes.append(linea)
        return puntajes

    def draw_ranking(self):
        linea = 100
        for puntaje in self.puntajes_juego:
            actual = font.render({puntaje}, True, "White")
            self.pantalla.blit(actual, (180, linea))
            linea += 50
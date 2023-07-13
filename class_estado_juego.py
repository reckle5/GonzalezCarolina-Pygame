import pygame,sys,json,os
from nivel_1 import *
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
from class_bandera import *
from pygame import mixer



class EstadoJuego():
    def __init__(self):

        self.estado_juego = "menu"
        self.debug = False
        self.clock = pygame.time.Clock()

        #####   SPRITES  #####

        #GRUPO PERSONAJE
        self.player_group = pygame.sprite.Group()
        self.proyectil_group = pygame.sprite.Group()
        self.personaje_juego =  Spidey(tamaño_personaje,dic_animaciones,coordenadas,15)
        self.player_group.add(self.personaje_juego)
        self.teclas_presionadas = {}
        self.list_ranking = []
        self.font = font
        self.nombre_actual = ""
        self.nombre_anterior = ""
        self.nombre_mas_alto = ""

        #GRUPO ENEMIGOS
        self.goomba_group = pygame.sprite.Group()
        self.tortuga_group = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.tortuga = Enemy((50,50),animaciones_tortuga,(4000, 250),10)
        self.donkey = Enemy((100,100),animaciones_donkey,(600,210),10)
        self.tortuga_group.add(self.tortuga)
        self.all_enemies.add(self.goomba_group)
        self.all_enemies.add(self.tortuga_group)

        #BANDERA LVL 1
        self.bandera_group = pygame.sprite.Group()
        self.bandera = Bandera(flag,(9460,176), bola_rect,palo_rect)
        self.bandera_group.add(self.bandera)

        #GRUPO PLATAFORMAS
        self.plataformas_group = pygame.sprite.Group()
        self.plataformas_sorpresa_group = pygame.sprite.Group()
        self.all_plataformas = pygame.sprite.Group()
        self.plataforma_boost =  pygame.sprite.Group()
        self.plataforma_escalera = pygame.sprite.Group()
        self.plataforma_booster_group = pygame.sprite.Group()


        #GRUPO OBJETOS INTERACTIVOS
        self.moneda_group = pygame.sprite.Group()
        self.hongo_boost = pygame.sprite.Group()

        #FONDO
        self.fondo = Background(fondo_img, WIDTH,(ancho_1,alto_1))
        self.fondo_lvl_2 = Background(fondo_2,WIDTH,(900,900))

        #PLATAFORMA PISO
        self.piso_1 = Piso(self.personaje_juego,0,700,3310,40)
        self.piso_2 = Piso(self.personaje_juego,3405,700,730,40)
        self.piso_3 = Piso(self.personaje_juego,4280,700,2135,40)
        self.piso_4 = Piso(self.personaje_juego,6622,700,90,40)
        self.piso_5 = Piso(self.personaje_juego,6900,700,200,40)
        self.piso_6 = Piso(self.personaje_juego,7450,700,4000,40)

        self.lista_plat_piso = [ self.piso_1,
                            self.piso_2,
                            self.piso_3,
                            self.piso_4,
                            self.piso_5,
                            self.piso_6]
        
        self.piso_2_1 =  Piso(self.personaje_juego,450,900,900,30)
        self.piso_2_2 =  Generar_rects(450,758,830,30)
        self.piso_2_3 =  Generar_rects(510,640,870,30)
        self.piso_2_4 =  Generar_rects(450,500,830,30)
        self.piso_2_5 =  Generar_rects(510,410,870,30)
        self.piso_2_6 =  Generar_rects(450,300,830,30)

        self.lista_piso_lvl_2 = [self.piso_2_1,
                            self.piso_2_2,
                            self.piso_2_3,
                            self.piso_2_4,
                            self.piso_2_5,
                            self.piso_2_6]
        
        self.piso_lvl_2 = pygame.sprite.Group()
        self.piso_lvl_2.add(self.lista_piso_lvl_2)
        self.topes_lvl_2 = pygame.sprite.Group()
        self.topes_lvl_2.add(topes_lvl2)

        agregar_a_grupo(lista_plat_sorpresa,self.plataformas_sorpresa_group)
        agregar_a_grupo(lista_plat_ladrillo,self.plataformas_group) 
        agregar_a_grupo(self.lista_plat_piso, self.plataformas_group)

        self.plataforma_escalera.add(lista_escalera)
        self.plataforma_booster_group.add(plataforma_caja8)
        self.all_plataformas.add(self.plataformas_sorpresa_group)
        self.all_plataformas.add(self.plataformas_group)
        self.all_plataformas.add(topes)
        self.all_plataformas.add(self.plataforma_booster_group)
        self.all_plataformas.add(self.plataforma_escalera)

        #MONEDAS
        self.moneda_group.add(self.personaje_juego.crear_moneda((1315,500)))
        self.moneda_group.add(self.personaje_juego.crear_moneda((1365,450)))
        self.moneda_group.add(self.personaje_juego.crear_moneda((1415,500)))
        self.coin_score = Coin((25,25),moneda,(910,10))

        #next level
        self.next_level_group =  pygame.sprite.Group()
        self.next_level_group.add(next_lvl)
        #All Sprites 
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player_group)
        self.sprites.add(self.proyectil_group)
        self.sprites.add(self.all_enemies)
        self.sprites.add(self.all_plataformas)
        self.sprites.add(self.moneda_group)
        self.sprites.add(self.plataforma_boost)
        self.sprites.add(self.hongo_boost)

        #SONIDOS
        self.jump_play = mixer.Sound("./src/recursos/sonidos/Jump.wav")
        self.game_over_play = mixer.Sound("./src/recursos/sonidos/Game Over.wav")

        

    def main_menu(self,pantalla,):

        fondo_menu = pygame.surface.Surface((1800,900))
        fondo_menu.fill("Black")
        pantalla.blit(fondo_menu, (0,0))
        pygame.display.set_caption("Menu")

        pantalla.blit(menu,(550,200))
        
        boton_inicio = Boton("START GAME", color_base, "White",800, 460, 160,30)
        boton_salir = Boton("QUIT",color_base, "White",800, 520, 100,30)

        self.evento_botnes(pantalla, boton_inicio,boton_salir,"nivel 1")
        if boton_inicio:
            pantalla.blit(self.fondo.image, (0,0))



        pygame.display.flip()


    def game_over(self,pantalla):

        fondo_over = pygame.surface.Surface((1800,900))
        fondo_over.fill("Black")

        msj = font.render("GAME OVER", True, "White")

        pantalla.blit(fondo_over, (0,0))
        pantalla.blit(msj, (800,450))

        pygame.display.set_caption("Game over ")

        boton_return = Boton("RESTART GAME",color_base, "White",800, 520, 60,20)
        boton_salir = Boton("QUIT",color_base, "White",800, 570, 60,20)

        self.evento_botnes(pantalla,boton_return,boton_salir,"menu")



        pygame.display.flip()

    def evento_botnes(self,pantalla,boton_1,boton_2,estado:str):
        pos = pygame.mouse.get_pos()

        for b in [boton_1,boton_2]:
            b.seleccionar_texto(pos)
            if b.spidey_visible:
                pantalla.blit(select_spidey, (b.rect.x - 50, b.rect.y - 15))
            pantalla.blit(b.text, b.rect)
        if boton_1.seleccionar_texto(pos):
            pantalla.blit(boton_1.text, boton_1.rect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_1.draw(pos):
                    self.estado_juego = estado
                if boton_2.draw(pos):
                    pygame.quit()
                    sys.exit()

    def nivel_1(self,pantalla):
        self.handler_events()
        self.update_1(pantalla)
        if self.personaje_juego.siguiente_nivel:
            self.personaje_juego.vida_actual = 900
            self.personaje_juego.rect.x = x_inicial
            self.personaje_juego.rect.y = y_inicial
            self.velocidad = 15
            self.estado_juego = "escribir score"

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

        elif pygame.K_RIGHT in self.teclas_presionadas :
            print(self.personaje_juego.colision)
            if self.estado_juego == "nivel 1":
                if self.personaje_juego.lados["main"].x < WIDTH - self.personaje_juego.velocidad - self.personaje_juego.lados["main"].x:
                    self.personaje_juego.que_hace = "derecha"
                else:
                    self.personaje_juego.velocidad = 0
                    self.personaje_juego.que_hace = "derecha"
                if self.personaje_juego.lados["main"].x > self.fondo.start_scrolling and not self.personaje_juego.colision: 
                    self.fondo.desplazamiento_derecha = True       
                    self.fondo.desplazamiento_izquierda = False
                    self.fondo.desplazamiento_x(-20) 
                elif self.personaje_juego.lados["main"].x > self.fondo.start_scrolling and self.personaje_juego.colision:       
                    self.fondo.desplazamiento_derecha = False       
                    self.fondo.desplazamiento_izquierda = False
                    self.fondo.desplazamiento_x(0)   
            if self.estado_juego == "nivel 2":
                self.personaje_juego.velocidad = 15
                self.personaje_juego.que_hace = "derecha"

        elif pygame.K_LEFT in self.teclas_presionadas: 
            if self.estado_juego == "nivel 1":
                if self.personaje_juego.lados["main"].x < WIDTH - self.personaje_juego.velocidad - self.personaje_juego.lados["main"].x: 
                    self.personaje_juego.que_hace = "izquierda"
                else:
                    self.personaje_juego.velocidad = 0
                    self.personaje_juego.que_hace = "izquierda"
                if self.personaje_juego.lados["main"].x > self.fondo.start_scrolling and not self.personaje_juego.colision:
                    self.fondo.desplazamiento_derecha = False
                    self.fondo.desplazamiento_izquierda = True
                    self.fondo.desplazamiento_x(20)
                elif self.personaje_juego.lados["main"].x > self.fondo.start_scrolling and self.personaje_juego.colision:       
                    self.fondo.desplazamiento_derecha = False       
                    self.fondo.desplazamiento_izquierda = False
                    self.fondo.desplazamiento_x(0)   
            if self.estado_juego == "nivel 2":
                self.personaje_juego.velocidad = 15
                self.personaje_juego.que_hace = "izquierda"

        elif pygame.K_UP in self.teclas_presionadas and self.personaje_juego.saltos_realizados != 0:
                    self.jump_play.play()
                    self.personaje_juego.colision = False
                    self.personaje_juego.que_hace = "salta"
                    self.personaje_juego.saltos_realizados -= 1
                    self.clock.tick(60)

        elif pygame.K_DOWN in self.teclas_presionadas: 
            self.personaje_juego.que_hace = "defensa"

        elif pygame.K_SPACE in self.teclas_presionadas  and self.personaje_juego.cooldown_proyectil == 0:
            self.clock.tick(60)
            self.personaje_juego.que_hace = "dispara"   
            self.proyectil_group.add(self.personaje_juego.crear_proyectil()) 
            self.personaje_juego.cooldown_proyectil = 1
        
            
        else:
            self.personaje_juego.que_hace = "quieto"


    def generar_enemigos(self,cantidad):
        if len(self.goomba_group) == 0:
            for i in range(cantidad):
                x = random.randrange(2500, 1089, -1)
                enemigo_1 = Enemy(tamaño_goomba, animaciones_goomba, (x,810),10)
                self.goomba_group.add(enemigo_1)
                self.all_enemies.add(enemigo_1)

    def update_1(self,pantalla):
        if self.estado_juego == "nivel 1":
            pantalla.blit(self.fondo.image, (0,0))
            self.generar_enemigos(2)
            self.tortuga.encapsular(topes,8)
            coin_score.animar_moneda(pantalla)
            self.proyectil_group.draw(pantalla)

            if self.personaje_juego.estado_vida:
                self.estado_juego = "game over"
                self.game_over_play.play()
            
            if self.debug == True:

                for lado in self.personaje_juego.lados:
                    pygame.draw.rect(pantalla, "Orange", self.personaje_juego.lados[lado], 3)

                for enemigo in self.all_enemies:
                    enemigo.draw_rect(pantalla)
                
                for plataformas in self.all_plataformas:
                    plataformas.draw_rect(pantalla,(r,g,b))
                
                for ban in self.bandera_group:
                    ban.draw_rect(pantalla)

                for i in self.next_level_group:
                    i.draw_rect(pantalla,(r,g,b))

            self.hongo_boost.update(pantalla,self.fondo,self.personaje_juego)
            self.all_enemies.update(pantalla,self.fondo,self.personaje_juego,2,self.all_plataformas)
            self.bandera_group.update(self.personaje_juego,self.fondo,pantalla,piso_bandera)
            self.moneda_group.update(pantalla,self.fondo,self.personaje_juego)
            self.proyectil_group.update(velocidad_proyectil,self.proyectil_group,self.all_enemies,self.personaje_juego)
            self.all_plataformas.update(pantalla,self.fondo,self.personaje_juego)
            self.next_level_group.update(pantalla,self.fondo,self.personaje_juego)
            self.personaje_juego.update(pantalla,self.all_enemies,self.all_plataformas,self.plataformas_sorpresa_group,self.plataformas_group,self.moneda_group,self.plataforma_booster_group,self.hongo_boost,self.plataforma_escalera,self.all_plataformas,self.next_level_group)

            pygame.display.flip()
    
    def update_2(self,pantalla):

        if self.estado_juego == "nivel 2":
            fondo_over = pygame.surface.Surface((1800,900))
            fondo_over.fill("Black")
            pantalla.blit(fondo_over, (0,0))
            pantalla.blit(self.fondo_lvl_2.image, (450,0))
            self.donkey.encapsular(self.topes_lvl_2,8)


            if self.personaje_juego.estado_vida:
                    self.estado_juego = "game over"

            if self.debug == True:
                for piso in self.piso_lvl_2:
                    piso.draw_rect(pantalla, "White")
                
                for tope in self.topes_lvl_2:
                    tope.draw_rect(pantalla, "White")

            self.personaje_juego.update(pantalla,self.all_enemies,self.piso_lvl_2,self.plataformas_sorpresa_group,self.plataformas_group,self.moneda_group,self.plataforma_booster_group,self.hongo_boost,self.plataforma_escalera,self.piso_lvl_2,self.next_level_group)
            self.donkey.update(pantalla,self.fondo_lvl_2,self.personaje_juego,1,self.piso_lvl_2)
            pygame.display.flip() 

    def cambiar_modo(self):
        self.debug = not self.debug
    
    def nivel_2(self,pantalla):
        self.handler_events()
        self.update_2(pantalla)

    def manejo_de_estado(self,pantalla):
        if self.estado_juego == "menu":
            self.main_menu(pantalla)
        elif self.estado_juego == "nivel 1":
            self.nivel_1(pantalla)
        # elif self.estado_juego == "nivel 2":
        #     self.nivel_2(pantalla)
        elif self.estado_juego == "game over":
            self.personaje_juego.estado_vida = False
            self.personaje_juego.vida_actual = 900
            self.personaje_juego.rect.x = x_inicial
            self.personaje_juego.rect.y = y_inicial
            self.velocidad = 15
            self.game_over(pantalla)
        elif self.estado_juego == "escribir score":
            self.score(pantalla)
        elif self.estado_juego == "ranking":
            self.personaje_juego.siguiente_nivel = False
            self.personaje_juego.estado_vida = False
            self.personaje_juego.vida_actual = 900
            self.personaje_juego.rect.x = x_inicial
            self.personaje_juego.rect.y = y_inicial
            self.velocidad = 15
            self.print_ranking(pantalla)

        pygame.display.flip()
    
    def score(self,pantalla):
        img_score = pygame.image.load("./src/recursos/score.jpg").convert_alpha()
        img_score = pygame.transform.scale(img_score,(1800,900))
        pantalla.blit(img_score, (0,0))
        self.draw_text(font_ranking,"INGRESE SUS INICIALES\nY PRESIONE ENTER" , "Black", 1200, 300,pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.TEXTINPUT:
                self.nombre_actual += event.text
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.guardar_ranking()
                    self.estado_juego = "ranking"

        self.draw_text(font_ranking_bold,self.nombre_actual , "Black", 1200, 400,pantalla)
        
        pygame.display.flip()


    def guardar_ranking(self):

        if os.path.exists("score.json"):    
            with open("score.json", "r") as file:
                self.list_ranking = json.load(file)
        else:
            self.list_ranking = []
        dic_ranking = {}
        dic_ranking["nombre"] = self.nombre_actual
        dic_ranking["score"] = self.personaje_juego.puntaje

        self.list_ranking.append(dic_ranking)
        print(self.list_ranking)

        with open("score.json", "w") as file:
            json.dump(self.list_ranking, file)
    
    def print_ranking(self,pantalla):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        img_score = pygame.image.load("./src/recursos/score.jpg").convert_alpha()
        img_score = pygame.transform.scale(img_score,(1800,900))
        pantalla.blit(img_score, (0,0))
        self.draw_text(font_ranking,"SPIDEY RANKING" , "Black", 1000, 300,pantalla)

        ranking = self.leer_archivo_json("score.json")
        ranking_ordenado = ordenar_ranking(ranking,False)
        self.imprimir_archivo_json(ranking_ordenado,pantalla)

        boton_return = Boton("RESTART GAME",color_base, "Black",1400, 700, 60,20)
        boton_salir = Boton("QUIT",color_base, " Black",1400, 760, 60,20)

        self.evento_botnes(pantalla,boton_return,boton_salir,"menu")

    def draw_text(self,fuente,text, text_col, x, y,pantalla):
        img = fuente.render(text, True, text_col)
        ancho = img.get_width()
        pantalla.blit(img, (x - (ancho/ 2), y))

    def leer_archivo_json(self,nombre_archivo:str)->list:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos

    def imprimir_archivo_json(self,datos:list,pantalla)->str:
        score_y = 350
        for i in range(5):
            if i < len(datos):
                self.draw_text(font_ranking_bold,datos[i]["nombre"] + ":" + str(datos[i]["score"]), "Black", 1200, score_y,pantalla)
                score_y += 50

def ordenar_ranking(lista:list, asc =True)->list:

    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i+1, tam):
            if (asc and lista[i]["score"] > lista[j]["score"]) or (not asc and lista[i]["score"] < lista[j]["score"]):   
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux  
    return lista


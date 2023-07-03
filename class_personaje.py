from sprites_personaje import *
from config import *


dic_animaciones = {}
dic_animaciones["quieto"] = personaje_quieto
dic_animaciones["salta"] = personaje_salta
dic_animaciones["camina_derecha"] = personaje_camina_derecha
dic_animaciones["camina_izquierda"] = personaje_camina_izquierda
dic_animaciones["personaje_defensa"] = personaje_defensa
dic_animaciones["personaje_ataca"] = personaje_ataque
def actualizar_pantalla(pantalla, personaje, fondo):
    pantalla.blit(fondo, (0,0))

    personaje.update(pantalla)

class Spidey:
    def __init__(self, tamaño:tuple, animaciones:list, posicion_inicial:tuple, velocidad:int):
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.size = (self.ancho,self.alto)
        #VELOCIDAD
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #GRAVEDAD 
        self.gravedad = 1
        self.potencia = -15
        self.limite_vel_caida = 15
        self.esta_saltando = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            (self.animaciones[clave], self.size)
        
    def animar_personaje(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1 
    
    def mover_personaje(self,velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def aplicar_gravedad(self,pantalla,plataformas):
        if self.esta_saltando:
            self.animar_personaje(pantalla, "salta")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_vel_caida:
                self.desplazamiento_y += self.gravedad

        for piso in plataformas:
            if self.lados['bottom'].colliderect(piso['top']):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados['main'].bottom = piso['main'].top
                break
            else:
                self.esta_saltando = True

    def update(self,pantalla,plataformas):
        match self.que_hace:
            case "derecha":
                if not esta_saltando:
                    self.animar_personaje(pantalla,"camina_derecha")
                self.mover_personaje(self.velocidad)
            case "izquierda":
                if not esta_saltando: 
                    self.animar_personaje(pantalla,"camina_izquierda")
                self.mover_personaje(self.velocidad * -1 )
                self.posicion -= 1
            case "salta":  
                esta_saltando = True
                self.desplazamiento_y = self.potencia
            case "defensa" :
                if not esta_saltando: 
                    self.animar_una_vez(pantalla, "personaje_defensa" )  
            case "dispara" : 
                if not esta_saltando:
                    self.animar_personaje(pantalla,"personaje_ataca")
            case "quieto": 
                if not esta_saltando:
                    self.animar_una_vez(pantalla, "quieto" )  
        
        self.aplicar_gravedad(pantalla,plataformas)


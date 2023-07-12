import pygame
from config import *

pantalla_juego = pygame.display.set_mode((WIDTH,HEIGHT))

menu = pygame.image.load("./src/recursos/menu/main-menu.jpg").convert()
menu = pygame.transform.scale(menu, (600,200))

select_spidey = pygame.image.load("./src/recursos/menu/0.png").convert()
select_spidey  = pygame.transform.scale(select_spidey , (40,40))


class Boton():
	
	def __init__(self, text_input, color_base,color_hover,x,y,w,h):

		self.image = pygame.Rect((x,y,w,h))
		self.rect = self.image
		self.rect.x = x
		self.rect.y = y
		self.clicked = False
		self.font = font
		self.base_color, self.hovering_color =  color_base,color_hover
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.spidey_visible = False

	def draw(self,pos):
		action = False

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
	
		return action
    
	def seleccionar_texto(self, position):
		if position[0] in range(self.rect.left, self.rect.right):
			self.spidey_visible = True
		elif not position[0] in range(self.rect.left, self.rect.right):
			self.select_spidey = False

		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


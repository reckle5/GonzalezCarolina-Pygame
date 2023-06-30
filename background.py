import pygame
from pygame.locals import *
from config import *

# bg_width = bg.get_width() * 3
# bg_height = bg.get_height() * 4
# bg = pygame.transform.scale(bg,(bg_width,bg_height))
stage_width = WIDTH + 400


class Background():
    def __init__(self,backg, width,player):
        # super().__init__()

        self.image = backg
        self.bg_width = self.image.get_width() * 3
        self.bg_height = self.image.get_height() * 4
        self.image = pygame.transform.scale(self.image,(self.bg_width, self.bg_height))
        self.floor = pygame.Rect(0,850,1500,40)
        self.floor2 = pygame.Rect(1800,850,1000,40)
        self.flor2 = player.rect.bottom
        self.floor_top = player.rect.bottom
        self.start_scrolling = width // 2

    def scrollX(self, offsetX):
        copy_bg = self.image.copy()
        self.image.blit(copy_bg, (offsetX, 0))
        if offsetX < 0:
            self.image.blit(copy_bg, (self.bg_width + offsetX, 0), (0, 0, -offsetX, self.bg_height))
        else:
            self.image.blit(copy_bg, (0, 0), (self.bg_width - offsetX, 0, offsetX, self.bg_height))

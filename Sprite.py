import pygame
import sys
import os
import time
from pygame import mixer
from pygame.locals import *


def showStartScreen(surface):
    show = True
    while show == True:
        start= pygame.image.load(os.path.join('images','Starting_scr.png'))
        surface.blit(start, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                show = False

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        self.imagesleft = []
        self.imagesright = []
        self.alpha = (0,0,0)
        self.ani = 4 # animation cycles
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(self.alpha)
            self.imagesright.append(img)
            self.image = self.imagesright[0]
            self.rect  = self.image.get_rect()
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img = pygame.transform.flip(img, True, False)
            img.convert_alpha()
            img.set_colorkey(self.alpha)
            self.imagesleft.append(img)
            self.image = self.imagesleft[0]
            self.rect  = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey -= y

    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = self.imagesleft[self.frame//self.ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = self.imagesright[self.frame//self.ani]


import pygame
import sys
import os
import time
from pygame import mixer
from pygame.locals import *
from settings import *
vec = pygame.math.Vector2

def showStartScreen(surface):
    show = True
    while (show == True):
        background = pygame.image.load(os.path.join('images', 'Starting_scr.png'))
        # rect = surface.get_rect()
        surface.blit(background, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                show = False

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.jumping = False
        self.images = []
        self.imagesleft = []
        self.imagesright = []
        self.direction = "right"
        self.alpha = (0,0,0)
        self.ani = 4 # animation cycles
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullet_timer = .1

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

    def update(self, dt):
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
            self.direction = "left"

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = self.imagesright[self.frame//self.ani]
            self.direction = "right"

        #enemy_hit_list = pygame.sprite.spritecollide(self,enemy_list, False)
        #for enemy in enemy_hit_list:
            #self.health -= 1
            #print(self.health)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bullet_timer -= dt  # Subtract the time since the last tick.

        if self.bullet_timer <= 0:
            self.bullet_timer = 100  # Bullet ready.
            if keys:  # Left mouse button.
                # Create a new bullet instance and add it to the groups.
                if self.direction == "right":
                    Bullet([self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2], self.direction, self.all_sprites)
                else:
                    Bullet([self.rect.x, self.rect.y + self.image.get_height()/2], self.direction, self.all_sprites)
                self.bullet_timer = .1  # Reset the timer.


class Bullet(pygame.sprite.Sprite):

    IMAGE = None
    FLIPPED_IMAGE = None

    def __init__(self, pos, direction, *sprite_groups):
        super().__init__(*sprite_groups)

        # cache images
        if not Bullet.IMAGE:
            Bullet.IMAGE = pygame.image.load(os.path.join('images','fireball.png'))
            Bullet.FLIPPED_IMAGE = pygame.transform.flip(Bullet.IMAGE, True, False)

        if direction == "right":
            self.vel = pygame.math.Vector2(750, 0)
            self.image = Bullet.IMAGE
        else:
            self.vel = pygame.math.Vector2(-750, 0)
            self.image = Bullet.FLIPPED_IMAGE

        self.pos = pygame.math.Vector2(pos)
        self.rect  = self.image.get_rect(center=pos)

    def update(self, dt):
        # Add the velocity to the position vector to move the sprite
        self.pos += self.vel * dt
        self.rect.center = self.pos  # Update the rect pos.
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()

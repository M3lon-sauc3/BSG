import pygame
import os
import sys
import time
from pygame import mixer
from Sprite1 import *
from settings import *

'''
Setup
'''
pygame.init()

clock = pygame.time.Clock()

pygame.mixer.music.load('.\\sounds\\Fairy.mp3')
pygame.mixer.music.play(-1, 0.0)

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

player.rect.x = 50
player.rect.y = 500




showStartScreen(surface)

'''
Main loop
'''

main = True

while main == True:

    background = pygame.image.load(os.path.join('images', 'Bg.png'))
    surface.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)

    keys = pygame.key.get_pressed()
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            player.rect.y -= (jumpCount * abs(jumpCount)) * 1
            jumpCount -= 2
        else:
            jumpCount = 10
            isJump = False

    # dt = time since last tick in milliseconds.
    dt = clock.tick(60) / 1000
    all_sprites.update(dt)
    player.update(dt)
    all_sprites.draw(surface) #refresh player position
    pygame.display.flip()


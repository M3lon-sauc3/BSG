import pygame
import os
import time
from pygame import mixer
import Sprite

'''
Objects
'''

'''
Setup
'''
width = 960
height = 720

fps = 40        # frame rate
#ani = 4        # animation cycles
clock = pygame.time.Clock()
pygame.init()
main = True

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISLAYSURF = pygame.display.set_mode((width,height))

surface = pygame.display.set_mode([width,height])
pygame.display.set_caption('B.S.G.!!!')
background = pygame.image.load(os.path.join('images','Bg.png')).convert()
backdropbox = surface.get_rect()
pygame.mixer.music.load('.\\sounds\\Fairy.mp3')
pygame.mixer.music.play(-1, 0.0)

player = Sprite.Player()   # spawn player
player.rect.x = 50
player.rect.y = 500
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10      # how fast to move

Sprite.showStartScreen(surface)
'''
Main loop
'''
while main == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.rect.y -= 100

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.rect.y += 100
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    surface.blit(background, (0, 0))
    player.update()
    player_list.draw(surface) #refresh player position
    pygame.display.flip()
    clock.tick(fps)
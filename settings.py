import pygame
isJump = False
jumpCount = 10
width = 960
height = 720
fps = 40        # frame rate
#ani = 4        # animation cycles
pygame.display.set_caption('B.S.G.')
surface = pygame.display.set_mode((width, height))
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
RED = (255, 0, 0)

steps = 10      # how fast to move
import pygame, sys
from pygame.locals import *
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
SCREENWIDTH = 800
SCREENHEIGHT = 800
RED = (255, 0, 0)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

while True:
    pygame.draw.rect(screen, RED, (400, 400, 20, 20), 0)
    screen.fill(RED)
    pygame.display.update()

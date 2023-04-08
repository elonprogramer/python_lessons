# Ширина окна
import sys

import pygame

screenWidth = 600
# Высота окна
screenHeight = 400

BLACK = (0, 0, 0)
GREEN = (124, 252, 0)

pygame.init()

# Окно
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Таймер
clock = pygame.time.Clock()

posX = 20
posY = 50

speed = 2



while True:
    screen.fill(BLACK)
    # Назначим FPS
    clock.tick(25)
    pygame.draw.circle(screen, GREEN, (posX, posY), 10)
    posX =posX + speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

# Ширина окна
import sys
import pygame

screenWidth = 800
# Высота окна
screenHeight = 600

BLACK = (0, 0, 0)
GREEN = (0, 103, 71)
BROWN = (205, 127, 50)

pygame.init()

# Окно
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Таймер
clock = pygame.time.Clock()

posX = 0
posY = 50

speed = 5

while True:
    screen.fill(GREEN)
    # Назначим FPS
    clock.tick(25)
    posX = posX + speed
    pygame.draw.rect(screen, BROWN, pygame.Rect(posX, 550, 10, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

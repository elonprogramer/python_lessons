# Ширина окна
import sys

import pygame
import random

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

speed = 5
speedY = 5
ball_radius = 20
c_speed = 5
c_one = 10

while True:
    screen.fill(BLACK)
    # Назначим FPS
    clock.tick(20)
    c_one = c_one + c_speed
    print(c_one)
    if c_one > 240:
        c_speed = -c_speed
    elif c_one < 10:
        c_speed = -c_speed
    pygame.draw.circle(screen, (c_one, c_one, c_one), (posX, posY), ball_radius)
    posX = posX + speed
    posY = posY + speedY
    if posX > screenWidth - ball_radius:
        speed = -speed
    elif posX < ball_radius:
        speed = -speed
    else:
        posY = posY + speedY
    if posY > screenHeight - ball_radius:
        speedY = -speedY
    elif posY < ball_radius:
        speedY = -speedY
    #else:
    #    speed = 4
    #    posX = posX - speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

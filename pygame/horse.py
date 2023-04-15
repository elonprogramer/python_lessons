# Ширина окна
import os
import pygame
from sys import exit as exit
# Импортируем  папку с картинками
images_folder = './images'
horseStand = pygame.image.load(os.path.join(images_folder, 'horse_stand.png'))
horseJump = pygame.image.load(os.path.join(images_folder, 'horse_jump.png'))
screenWidth = 800
# Высота окна
screenHeight = 600

BLACK = (0, 0, 0)
GREEN = (0, 103, 71)
BROWN = (205, 127, 50)


class Wall(object):
    def __init__(self, x, y, color, height, speed):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = 10
        self.speed = speed


black_big_wall = Wall(x=0, y=550, color=BLACK, height=75, speed=5)

pygame.init()

# Окно
screen = pygame.display.set_mode((screenWidth, screenHeight))
print('window started')

# Таймер
clock = pygame.time.Clock()

# wallX = 0
# wallY = 550

speed = 5

while True:
    screen.fill(GREEN)
    # Назначим FPS
    clock.tick(25)
    black_big_wall.x = black_big_wall.x + speed
    if black_big_wall.x > screenWidth:
        black_big_wall.x = 0
    horseY = 550
    horseX = int(screenWidth / 2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        horseY = horseY - 55
        screen.blit(horseJump, (horseX, horseY))
    else:
        if horseY != 550:
            horseY = 550
        screen.blit(horseStand, (horseX, horseY))
    print(horseY)
    pygame.draw.rect(screen, black_big_wall.color, pygame.Rect(black_big_wall.x, black_big_wall.y, black_big_wall.width, black_big_wall.height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

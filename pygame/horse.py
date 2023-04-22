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
YELLOW = (255, 215, 0)


class Wall(object):
    def __init__(self, x, y, color, height, speed):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = 10
        self.speed = speed


black_big_wall = Wall(x=0, y=550, color=BLACK, height=75, speed=5)
brown_small_wall = Wall(x=500, y=550, color=BROWN, height=50, speed=5)
yellow_small_wall = Wall(x=screenWidth, y=450, color=YELLOW, height=50, speed=10)
pygame.init()

# Окно
screen = pygame.display.set_mode((screenWidth, screenHeight))
# background_image = pygame.image.load(os.path.join(images_folder, "Без имени.jpeg"))

# background_image = pygame.transform.scale(background_image, (screenWidth, screenHeight))

print('window started')

# Таймер
clock = pygame.time.Clock()

# wallX = 0
# wallY = 550

speed = 5
yellow_small_wall_speed = 6
while True:
    screen.fill(GREEN)
    # Назначим FPS
    clock.tick(25)
    black_big_wall.x = black_big_wall.x + speed
    if black_big_wall.x > screenWidth:
        black_big_wall.x = 0
    brown_small_wall.x = brown_small_wall.x + speed
    if brown_small_wall.x > screenWidth:
        brown_small_wall.x = 0
    yellow_small_wall.x = yellow_small_wall.x - yellow_small_wall_speed
    if yellow_small_wall.x < 0:
        yellow_small_wall.x = screenWidth
    horseY = 550
    horseX = int(screenWidth / 2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        horseY = horseY - 100
        screen.blit(horseJump, (horseX, horseY))
    else:
        if horseY != 550:
            horseY = 550
        screen.blit(horseStand, (horseX, horseY))
    pygame.draw.rect(screen, black_big_wall.color, pygame.Rect(black_big_wall.x, black_big_wall.y, black_big_wall.width, black_big_wall.height))
    pygame.time.wait(5)
    pygame.draw.rect(screen, brown_small_wall.color, pygame.Rect(brown_small_wall.x, brown_small_wall.y, brown_small_wall.width, brown_small_wall.height))
    pygame.time.wait(5)
    pygame.draw.rect(screen, yellow_small_wall.color, pygame.Rect(yellow_small_wall.x, yellow_small_wall.y, yellow_small_wall.width, yellow_small_wall.height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

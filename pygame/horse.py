# Ширина окна
import os
from pathlib import Path

import pygame
from sys import exit as exit
# Импортируем папку с картинками

# получаем путь к папке, где лежит игра
BASE_DIR = Path(__file__).resolve().parent
# получаем путь к папке с картинками
images_folder = (os.path.join(BASE_DIR, 'images'))
music_folder = (os.path.join(BASE_DIR, 'sounds'))


horseStand = pygame.image.load(os.path.join(images_folder, 'horse_stand.png'))
horseJump = pygame.image.load(os.path.join(images_folder, 'horse_jump.png'))
horseFall = pygame.transform.rotate(horseStand, 180)

screenWidth = 800
# Высота окна
screenHeight = 600

BLACK = (0, 0, 0)
GREEN = (0, 103, 71)
BROWN = (205, 127, 50)
YELLOW = (255, 215, 0)
BLUE = (240, 248, 255)

HORIZONT_LEVEL = 550

# Создание класса для прямоугольных спрайтов
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Wall(object):
    def __init__(self, x, y, color, height, speed):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = 10
        self.speed = speed
        self.right_end_x = self.x + self.width


class Horse(object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state


# функция, которая определяет есть ли столкновение с черной стеной
def collision_detection(black_horse, black_big_wall):
    right_end_x = black_big_wall.x + black_big_wall.width
    wall_end_y = black_big_wall.y - black_big_wall.height
    if black_horse.y > wall_end_y:
        if black_horse.x == right_end_x:
            black_big_wall.speed = 0
        else:
            pass

black_big_wall = Wall(x=0, y=HORIZONT_LEVEL, color=BLACK, height=75, speed=1)

black_big_wall_sprite = Rectangle(BLUE, 10, 50)
black_big_wall_sprite.x = 200
black_big_wall_sprite.y = 500

sprites = pygame.sprite.Group()
sprites.add(black_big_wall_sprite)


brown_small_wall = Wall(x=screenWidth - 200, y=HORIZONT_LEVEL, color=BROWN, height=50, speed=3)
yellow_small_wall = Wall(x=screenWidth, y=HORIZONT_LEVEL - 100, color=YELLOW, height=50, speed=5)

black_horse = Horse(int(screenWidth / 2), 550, horseStand)

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

# music
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_folder, 'horse_topot.mp3'))
pygame.mixer.music.play(1000, 0)

while True:
    screen.fill(GREEN)
    # Назначим FPS
    clock.tick(60)

    sprites.draw(screen)

    black_big_wall.x = black_big_wall.x + black_big_wall.speed
    if black_big_wall.x > screenWidth:
        black_big_wall.x = 0
    brown_small_wall.x = brown_small_wall.x + speed
    if brown_small_wall.x > screenWidth:
        brown_small_wall.x = 0
    yellow_small_wall.x = yellow_small_wall.x - yellow_small_wall_speed
    if yellow_small_wall.x < 0:
        yellow_small_wall.x = screenWidth

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        black_horse.y = HORIZONT_LEVEL - 100
        black_horse.state = horseJump
        screen.blit(black_horse.state, (black_horse.x, black_horse.y))
        pygame.mixer.music.pause()
    else:
        if black_horse.y != 550:
            black_horse.y = 550
        black_horse.state = horseStand
        screen.blit(black_horse.state, (black_horse.x, black_horse.y))
        pygame.mixer.music.unpause()

    pygame.draw.rect(screen, black_big_wall.color, pygame.Rect(black_big_wall.x, black_big_wall.y, black_big_wall.width, black_big_wall.height))
    collision_detection(black_horse, black_big_wall)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

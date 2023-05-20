from time import sleep

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Example")

# Определение цветов
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Создание класса для прямоугольных спрайтов
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# Создание класса для спрайтов кругов
class Circle(pygame.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2], pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()

# Создание спрайтов
red_rectangle = Rectangle(RED, 100, 100)
red_rectangle.rect.x = 100
red_rectangle.rect.y = 200

yellow_circle = Circle(YELLOW, 50)
yellow_circle.rect.x = 500
yellow_circle.rect.y = 120

# Создание группы спрайтов
sprites = pygame.sprite.Group()
sprites.add(red_rectangle, yellow_circle)

clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиции желтого спрайта
    yellow_circle.rect.x -= 0.1

    # Проверка столкновения спрайтов
    if pygame.sprite.collide_rect(red_rectangle, yellow_circle):
        sleep(10)
        running = False

    # Заливка экрана зеленым цветом
    screen.fill(GREEN)

    # Отрисовка спрайтов
    sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()

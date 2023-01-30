import pygame
import random

pygame.init()

# Створюємо вікно
screen = pygame.display.set_mode((800, 600))

# Задаємо назву вікна
pygame.display.set_caption("Гонки")

# Задаємо зображення фону
background = pygame.image.load('background.jpg')

# Задаємо зображення автомобіля
carImg = pygame.image.load('car.webp')

# Задаємо початкові координати автомобіля
x = 30
y = 48
x_change = 0

# Задаємо початкові координати препятствів
obstacle_x = random.randint(0, 736)
obstacle_y = -600
obstacle_change_y = 4

# Задаємо функцію для відображення автомобіля
def car(x, y):
    screen.blit(carImg, (x, y))

# Задаємо функцію для відображення препятствів
def obstacle(obstacle_x, obstacle_y):
    screen.blit(obstacleImg, (obstacle_x, obstacle_y))

# Задаємо зображення препятствів
obstacleImg = pygame.image.load('obstacle.webp')

# Задаємо головний цикл програми
running = True
while running:
    # Задаємо колір фону
    screen.fill((0, 0, 0))
    # Задаємо фон
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Задаємо переміщення автомобіля
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_change
    # Задаємо межі переміщення автомобіля
    if x <= 0:
        x = 0
    elif x >= 736:
        x = 736
    # Задаємо переміщення препятствів
    obstacle_y += obstacle_change_y
    # Задаємоповернення препятствів на початкову позицію
    obstacle_height = 1
    if obstacle_y > 600:
        obstacle_y = 0 - obstacle_height
        obstacle_x = random.randint(0, 736)
    # Викликаємо функції для відображення автомобіля та препятствів
    car(x, y)
    obstacle(obstacle_x, obstacle_y)
    # Оновлюємо екран
    pygame.display.update()
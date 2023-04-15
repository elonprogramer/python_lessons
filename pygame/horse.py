# Ширина окна
import os
import pygame

# Импортируем  папку с картинками
images_folder = './images'
horseStand = pygame.image.load(os.path.join(images_folder, 'horse_stand.png'))
screenWidth = 800
# Высота окна
screenHeight = 600

BLACK = (0, 0, 0)
GREEN = (0, 103, 71)
BROWN = (205, 127, 50)

pygame.init()

# Окно
screen = pygame.display.set_mode((screenWidth, screenHeight))
print('window started')

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
    if posX > screenWidth:
        posX = 0
    horseY = screenHeight / 2
    horseX = int(screenWidth / 2)
    screen.blit(horseStand, (horseX, horseY))
    pygame.draw.rect(screen, BROWN, pygame.Rect(posX, 500, 10, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

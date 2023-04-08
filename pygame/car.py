import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("python_lessons/pygame/sounds/car_engine_sound.mpg")
pygame.mixer.music.play(1000, 0)
screen = pygame.display.set_mode([1000, 1000])
BLUE = (0, 0, 255)
running = True
while running:
    a = random.randint(0, 999)
    b = (0, 0, 255)
    for event in pygame.event.get():
        i = event.type
        print(i)
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    # Корпус машины
    if i != 1024:
        pygame.draw.rect(screen, b, pygame.Rect(70, 650, 780, 100))
    else:
        pygame.draw.rect(screen, b, pygame.Rect(70, 650, 780, 100))
    # Переднеё смтекло
    pygame.draw.line(screen, (0, 0, 255), (200, 650), (350, 500), 5)
    # Средняя линия
    pygame.draw.line(screen, (0, 0, 255), (500, 500), (500, 650), 5)
    # Заднеё стекло
    pygame.draw.line(screen, (0, 0, 255), (700, 500), (848, 650), 5)
    # 1 колесо
    pygame.draw.circle(screen, (0, 0, 0), (250, 750), 50)
    # 2 колесо
    pygame.draw.circle(screen, (0, 0, 0), (750, 750), 50)
    # Крыша
    pygame.draw.line(screen, (0, 0, 255), (350, 500), (700, 500), 10)
    # туловеще
    # pygame.draw.rect(screen, (0, a, 0), (400, 550), (400, 650), 30)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(370, 580, 60, 70))
    # Голова
    pygame.draw.circle(screen, (233, 150, 122), (400, 550), 30)
    # Труба
    pygame.draw.line(screen, (0, 0, 0), (848, 720), (900, 720), 10)
    pygame.display.flip()

pygame.quit()

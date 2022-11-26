import pygame
W, H = 600, 400
name = "Влад"
sc = pygame.display.set_mode((600, 400))
pygame.init()
pygame.display.set_mode((600, 400))
pygame.display.set_caption(f"{name}")


pygame.draw.rect(sc, (255, 255, 255), (10, 10, 50, 100))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print(name)
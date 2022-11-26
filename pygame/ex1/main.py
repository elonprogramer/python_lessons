import pygame
pygame.init()
pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Влад списує з гдз")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
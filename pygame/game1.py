# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
BLUE = (0, 0, 255)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    pygame.draw.line(screen, (255, 0, 0), (150, 140), (350, 140), 10)
    pygame.draw.line(screen, (255, 0, 0), (650, 140), (850, 140), 10)
    # Глаза
    pygame.draw.circle(screen, (255, 0, 0), (250, 250), 100)
    pygame.draw.circle(screen, (255, 0, 0), (750, 250), 100)
    # Зрачки
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50)
    pygame.draw.circle(screen, (0, 0, 255), (750, 250), 50)
    # eyebrow
    pygame.draw.line(screen, (255, 0, 0), (500, 400), (500, 450), 10)
    pygame.draw.line(screen, (255, 0, 0), (350, 650), (650, 650), 10)
#    pygame.draw.rect(screen, BLUE, (200,150,100,50))
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

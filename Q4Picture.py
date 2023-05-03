# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame, sys

pygame.init()

Display = pygame.display.set_mode((500, 500))

Clock = pygame.time.Clock()
FPS = 60

while True:
    Display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.polygon(Display, (24, 155, 204), [(0,0), 
    (500,0), (500,500), (0,500)])
    pygame.draw.polygon(Display, (255, 0, 0), [
    (250,50), (50, 200), (450,200)])
    pygame.draw.polygon(Display, (245, 245, 220),[(100, 400), 
    (100, 201), (400,201), (400,400)])
    pygame.display.flip()
    Clock.tick(FPS)
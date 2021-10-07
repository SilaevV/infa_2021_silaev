import pygame
from pygame.draw import *

pygame.init()

yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(white)

circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 1)
polygon(screen, black, [(103, 117), (183, 167), (178, 175), (99, 125)])
polygon(screen, black, [(220, 167), (299, 136), (301, 145), (223, 175)])
circle(screen, red, (150, 180), 20)
circle(screen, black, (150, 180), 20, 1)
circle(screen, red, (250, 180), 15)
circle(screen, black, (250, 180), 15, 1)
circle(screen, black, (150, 180), 8)
circle(screen, black, (250, 180), 7)
rect(screen, black, (150, 250, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

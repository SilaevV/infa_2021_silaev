import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 50
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    V_x = randint(-20, 20) 
    V_y = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    return(x, y, r, color, V_x, V_y)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
catched = False
score = 0
frame_number = 100
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_x, event_y = event.pos
            if (event_x - x) ** 2 + (event_y - y) **2 <= r ** 2:
                score += 1
                catched = True
                print(score)
    if frame_number == 100 or catched:
        x, y, r, color, V_x, V_y = new_ball()
        catched = False
        frame_number = 0
    if x <= r or x >= 1200 - r:
        V_x *= -1
    if y <= r or y >= 900 - r:
        V_y *= -1
    x += V_x
    y += V_y
    circle(screen, color, (x, y), r)
    pygame.display.update()
    screen.fill(BLACK)
    frame_number += 1

pygame.quit()

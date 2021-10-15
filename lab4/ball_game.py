import pygame
from pygame.draw import *
from random import randint
pygame.font.init()

pygame.init()

FPS = 50
screen = pygame.display.set_mode((1200, 900))
font1 = pygame.font.Font(None, 30)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    V_x = randint(-20, 20)
    V_y = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    return x, y, r, color, V_x, V_y


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
ball_age = [20, 40, 60, 80, 100]
x, y, r, color, V_x, V_y = [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5
ball_num = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_x, event_y = event.pos
            for ball_num in range(5):
                if (event_x - x[ball_num]) ** 2 + (event_y - y[ball_num]) ** 2 <= r[ball_num] ** 2:
                    score += 1
                    ball_age[ball_num] = 100
    for ball_num in range(5):
        if ball_age[ball_num] == 100:
            x[ball_num], y[ball_num], r[ball_num], color[ball_num], V_x[ball_num], V_y[ball_num] = new_ball()
            ball_age[ball_num] = 0
        if x[ball_num] <= r[ball_num] or x[ball_num] >= 1200 - r[ball_num]:
            V_x[ball_num] *= -1
        if y[ball_num] <= r[ball_num] or y[ball_num] >= 900 - r[ball_num]:
            V_y[ball_num] *= -1
        x[ball_num] += V_x[ball_num]
        y[ball_num] += V_y[ball_num]
        ball_age[ball_num] += 1
        circle(screen, color[ball_num], (x[ball_num], y[ball_num]), r[ball_num])
    score_text = font1.render('Your score: ' + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

import pygame
from pygame.draw import *
from model import *

print('Choose the maximum number of the balls on the screen:')
n = int(input())
balls_number(n)

from model import *

pygame.font.init()

pygame.init()

FPS = 50
screen = pygame.display.set_mode((1200, 900))
font1 = pygame.font.Font(None, 30)


clock = pygame.time.Clock()
finished = False
time = 1500
score = 0

while not finished and time != 0:
    clock.tick(FPS)
    time -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_x, event_y = event.pos
            score += ball_clicked(event_x, event_y, n)
    for ball_num in range(n):
        respawn_ball(ball_num, n)
        reflect_ball(ball_num)
        move_ball(ball_num)
        circle(screen, color[ball_num], (x[ball_num], y[ball_num]), r[ball_num])
    score_text = font1.render('Your score: ' + str(score), True, WHITE)
    time_text = font1.render(str(time // 50) + ' seconds remaining', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 35))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

file = open('tournament_table.txt', 'r')
table = [line.strip() for line in file]
file.close()
names = []
scores = []
for i in range(len(table)):
    name, best_score = table[i].split()
    names.append(name[:-1])
    scores.append(int(best_score))

print('Enter your name:')
name = input()
if name in names:
    if score > scores[names.index(name)]:
        i = 0
        while scores[i] > score:
            i += 1
        scores.pop(names.index(name))
        scores.insert(i, score)
        names.pop(names.index(name))
        names.insert(i, name)
elif len(names) != 0 and score >= scores[-1]:
    i = 0
    while scores[i] > score:
        i += 1
    scores.insert(i, score)
    names.insert(i, name)
else:
    names.append(name)
    scores.append(score)

file = open('tournament_table.txt', 'w')
for i in range(len(names)):
    file.write(names[i] + ': ' + str(scores[i]) + '\n')

file.close()
print('Tournament table has been updated')


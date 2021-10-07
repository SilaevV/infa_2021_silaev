import pygame
from pygame.draw import *

pygame.init()

sky_blue = (0, 255, 255)
grass_green = (0, 255, 0)
leaf_green = (0, 128, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
fruit_pink = (255, 170, 170)
pink = (229, 128, 255)
hair1 = (233, 175, 175)
hair2 = (233, 198, 175)
hair3 = (255, 238, 170)
hair4 = (229, 255, 128)
hair5 = (175, 233, 221)

FPS = 30
screen = pygame.display.set_mode((800, 1200))


def tree(x, y, size_x, size_y):
    rect(screen, white, ((100 - 100) * size_x + x, (630 - 870) * size_y + y, 50 * size_x, 150 * size_y))
    ellipse(screen, leaf_green, ((20 - 100) * size_x + x, (510 - 870) * size_y + y, 225 * size_x, 175 * size_y))
    ellipse(screen, leaf_green, ((15 - 100) * size_x + x, (170 - 870) * size_y + y, 220 * size_x, 240 * size_y))
    ellipse(screen, grass_green, ((20 - 100) * size_x + x, (510 - 870) * size_y + y, 225 * size_x, 175 * size_y), 3)
    ellipse(screen, grass_green, ((15 - 100) * size_x + x, (170 - 870) * size_y + y, 220 * size_x, 240 * size_y), 3)
    ellipse(screen, leaf_green, ((-70 - 100) * size_x + x, (340 - 870) * size_y + y, 400 * size_x, 200 * size_y))
    ellipse(screen, grass_green, ((-70 - 100) * size_x + x, (340 - 870) * size_y + y, 400 * size_x, 200 * size_y), 3)
    ellipse(screen, fruit_pink, ((10 - 100) * size_x + x, (440 - 870) * size_y + y, 30 * size_x, 30 * size_y))
    ellipse(screen, fruit_pink, ((170 - 100) * size_x + x, (240 - 870) * size_y + y, 30 * size_x, 30 * size_y))
    ellipse(screen, fruit_pink, ((275 - 100) * size_x + x, (455 - 870) * size_y + y, 30 * size_x, 30 * size_y))
    ellipse(screen, fruit_pink, ((210 - 100) * size_x + x, (640 - 870) * size_y + y, 30 * size_x, 30 * size_y))
    ellipse(screen, grass_green, ((10 - 100) * size_x + x, (440 - 870) * size_y + y, 30 * size_x, 30 * size_y), 3)
    ellipse(screen, grass_green, ((170 - 100) * size_x + x, (240 - 870) * size_y + y, 30 * size_x, 30 * size_y), 3)
    ellipse(screen, grass_green, ((275 - 100) * size_x + x, (455 - 870) * size_y + y, 30 * size_x, 30 * size_y), 3)
    ellipse(screen, grass_green, ((210 - 100) * size_x + x, (640 - 870) * size_y + y, 30 * size_x, 30 * size_y), 3)


def hair(coord_x, coord_y, size):
    ellipse(screen, hair2, (coord_x - 45 * size, coord_y + 12 * abs(size), 50 * abs(size), 30 * abs(size)))
    ellipse(screen, hair1, (coord_x - 65 * size, coord_y, 65 * abs(size), 20 * abs(size)))
    ellipse(screen, hair1, (coord_x - 95 * size, coord_y + 12 * abs(size), 65 * abs(size), 40 * abs(size)))
    ellipse(screen, hair2, (coord_x - 75 * size, coord_y + 60 * abs(size), 65 * abs(size), 30 * abs(size)))
    ellipse(screen, hair3, (coord_x - 110 * size, coord_y + 40 * abs(size), 90 * abs(size), 30 * abs(size)))
    ellipse(screen, hair4, (coord_x - 125 * size, coord_y + 60 * abs(size), 65 * abs(size), 25 * abs(size)))
    ellipse(screen, hair4, (coord_x - 72 * size, coord_y + 82 * abs(size), 85 * abs(size), 28 * abs(size)))
    ellipse(screen, hair3, (coord_x - 115 * size, coord_y + 80 * abs(size), 60 * abs(size), 23 * abs(size)))
    ellipse(screen, hair3, (coord_x - 100 * size, coord_y + 95 * abs(size), 75 * abs(size), 20 * abs(size)))
    ellipse(screen, hair5, (coord_x - 133 * size, coord_y + 90 * abs(size), 45 * abs(size), 15 * abs(size)))
    ellipse(screen, hair5, (coord_x - 133 * size, coord_y + 100 * abs(size), 70 * abs(size), 18 * abs(size)))
    ellipse(screen, hair3, (coord_x - 95 * size, coord_y + 105 * abs(size), 70 * abs(size), 20 * abs(size)))
    ellipse(screen, hair5, (coord_x - 65 * size, coord_y + 105 * abs(size), 62 * abs(size), 23 * abs(size)))
    ellipse(screen, pink, (coord_x - 160 * size, coord_y + 113 * abs(size), 90 * abs(size), 22 * abs(size)))


def unicorn(x, y, size):
    hair((190 - 645) * size + x, (860 - 655) * size + y, - size)
    hair((390 - 645) * size + x, (810 - 655) * size + y, size)
    ellipse(screen, white, ((375 - 645) * size + x, (750 - 655) * size + y, 310 * size, 130 * size))
    ellipse(screen, white, ((565 - 645) * size + x, (620 - 655) * size + y, 110 * size, 75 * size))
    ellipse(screen, white, ((620 - 645) * size + x, (645 - 655) * size + y, 100 * size, 50 * size))
    rect(screen, white, ((565 - 645) * size + x, (670 - 655) * size + y, 90 * size, 130 * size))
    rect(screen, white, ((395 - 645) * size + x, (845 - 655) * size + y, 20 * size, 155 * size))
    rect(screen, white, ((465 - 645) * size + x, (860 - 655) * size + y, 25 * size, 130 * size))
    rect(screen, white, ((565 - 645) * size + x, (870 - 655) * size + y, 22 * size, 150 * size))
    rect(screen, white, ((625 - 645) * size + x, (850 - 655) * size + y, 18 * size, 140 * size))
    circle(screen, pink, ((640 - 645) * size + x, (655 - 655) * size + y), 13 * size)
    circle(screen, black, ((645 - 645) * size + x, (655 - 655) * size + y), 5 * size)
    ellipse(screen, white, ((633 - 645) * size + x, (650 - 655) * size + y, 10 * size, 3 * size))
    hair((604 - 645) * size + x, (630 - 655) * size + y, size)
    polygon(screen, pink,
            [((606 - 645) * size + x, (621 - 655) * size + y), ((633 - 645) * size + x, (500 - 655) * size + y),
             ((635 - 645) * size + x, (625 - 655) * size + y)])
    ellipse(screen, hair1, ((575 - 645) * size + x, (610 - 655) * size + y, 50 * size, 30 * size))


rect(screen, sky_blue, (0, 0, 800, 520))
rect(screen, grass_green, (0, 520, 800, 1200))
circle(screen, yellow, (770, 120), 150)
for i in range(150):
    circle(screen, (255, 255, 155 - i), (770, 120), 150 - i)
tree(220, 600, 1, 1)
tree(350, 640, 0.7, 0.3)
tree(165, 870, 1, 0.7)
tree(40, 750, 0.7, 0.7)
tree(70, 1100, 0.7, 0.7)
unicorn(400, 800, 0.9)
unicorn(675, 655, 0.5)
unicorn(550, 450, 0.6)
unicorn(750, 480, 0.3)
unicorn(710, 900, 0.6)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

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

rect(screen, sky_blue, (0, 0, 800, 520))
rect(screen, grass_green, (0, 520, 800, 1200))
circle(screen, yellow, (770, 120), 150)

# tree
rect(screen, white, (100, 630, 50, 150))
ellipse(screen, leaf_green, (20, 510, 225, 175))
ellipse(screen, leaf_green, (-70, 340, 400, 200))
ellipse(screen, leaf_green, (15, 170, 220, 240))
circle(screen, fruit_pink, (10, 440), 30)
circle(screen, fruit_pink, (170, 240), 30)
circle(screen, fruit_pink, (275, 455), 30)
circle(screen, fruit_pink, (210, 640), 30)


# unicorn
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


hair(190, 860, -1)
hair(390, 810, 1)
ellipse(screen, white, (375, 750, 310, 130))
ellipse(screen, white, (565, 620, 110, 75))
ellipse(screen, white, (620, 645, 100, 50))
rect(screen, white, (565, 670, 90, 130))
rect(screen, white, (395, 845, 20, 155))
rect(screen, white, (465, 860, 25, 130))
rect(screen, white, (565, 870, 22, 150))
rect(screen, white, (625, 850, 18, 140))
circle(screen, pink, (640, 655), 13)
circle(screen, black, (645, 655), 5)
ellipse(screen, white, (633, 650, 10, 3))
hair(604, 630, 1)
polygon(screen, pink, [(606, 621), (633, 500), (635, 625)])
ellipse(screen, hair1, (575, 610, 50, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

from random import randint


def balls_number(n):
    global x, y, r, color, V_x, V_y
    for i in range(n):
        ball_age.append(50 * (i + 1))
    x, y, r, color, V_x, V_y = [0] * n, [0] * n, [0] * n, [0] * n, [0] * n, [0] * n


def new_ball():
    x_new = randint(100, 700)
    y_new = randint(100, 500)
    r_new = randint(30, 50)
    V_x_new = randint(-15, 15)
    V_y_new = randint(-15, 15)
    color_new = COLORS[randint(0, 5)]
    return x_new, y_new, r_new, color_new, V_x_new, V_y_new


def ball_clicked(event_x, event_y, n):
    click_score = 0
    for ball_num in range(n):
        if (event_x - x[ball_num]) ** 2 + (event_y - y[ball_num]) ** 2 <= r[ball_num] ** 2:
            click_score += 1
            ball_age[ball_num] = 50 * n
    return click_score


def respawn_ball(ball_num, n):
    global x, y, r, color, V_x, V_y
    if ball_age[ball_num] == 50 * n:
        x[ball_num], y[ball_num], r[ball_num], color[ball_num], V_x[ball_num], V_y[ball_num] = new_ball()
        ball_age[ball_num] = 0


def reflect_ball(ball_num):
    global x, y, r, color, V_x, V_y
    if x[ball_num] <= r[ball_num] or x[ball_num] >= 1200 - r[ball_num]:
        x[ball_num] -= V_x[ball_num]
        V_x[ball_num] *= - randint(25, 60) / 50
    if y[ball_num] <= r[ball_num] or y[ball_num] >= 900 - r[ball_num]:
        y[ball_num] -= V_y[ball_num]
        V_y[ball_num] *= - randint(25, 60) / 50


def move_ball(ball_num):
    x[ball_num] += V_x[ball_num]
    y[ball_num] += V_y[ball_num]
    ball_age[ball_num] += 1


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

ball_age = []

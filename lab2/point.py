import turtle

Vx = int(input())
Vy = int(input())
x, y = -400, -200
a = 10
dt = 0.1

turtle.shape('circle')
turtle.width(5)
turtle.speed(1000)
turtle.penup()
turtle.goto(400, -200)
turtle.pendown()
turtle.goto(-400, -200)
turtle.speed(1)
turtle.width(1)

while x <= 400:
    while y >= -200 and x <= 400:
        turtle.goto(x, y)
        x += Vx * dt
        y += Vy * dt - a * dt**2//2
        Vy -= a * dt
    Vx += 0.1 * Vy
    Vy = -0.8 * Vy
    y = -200

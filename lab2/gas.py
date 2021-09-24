from random import randint
import turtle
import math


number_of_turtles = 20
steps_of_time_number = 100

turtle.penup()
turtle.speed(1000)
turtle.goto(-400, -300)
turtle.width(5)
turtle.pendown()
turtle.goto(-400, 300)
turtle.goto(400, 300)
turtle.goto(400, -300)
turtle.goto(-400, -300)
turtle.hideturtle()

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(randint(290, 310))
    unit.goto(randint(-395, 395), randint(-295, 295))
    unit.left(randint(0, 360))


for i in range(steps_of_time_number):
    for unit in pool:
        x1 = unit.xcor()
        y1 = unit.ycor()
        unit.forward(2)
        x2 = unit.xcor()
        y2 = unit.ycor()
        if x2 > 395 or x2 < -395:
            unit.left(math.atan((x2-x1)/(y2-y1)) * 360 / math.pi)
        if y2 > 295 or y2 < -295:
            unit.left(-math.atan((y2-y1)/(x2-x1)) * 360 / math.pi)

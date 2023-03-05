from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    color_r = randint(0, 255)
    color_g = randint(0, 255)
    color_b = randint(0, 255)
    color = (color_r, color_g, color_b)
    return color


def draw_line():
    for _ in range(10):
        my_turtle.pendown()
        my_turtle.dot(20, random_color())
        my_turtle.penup()
        my_turtle.forward(50)


my_turtle = Turtle()
colormode(255)
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.penup()

ypos = -225
my_turtle.setpos(-225, ypos)
for _ in range(10):
    draw_line()
    ypos += 50
    my_turtle.setpos(-225, ypos)

my_screen = Screen()
my_screen.exitonclick()

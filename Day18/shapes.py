import turtle
from turtle import Turtle, Screen
import random


def random_color():
    color_r = random.randint(0, 255)
    color_g = random.randint(0, 255)
    color_b = random.randint(0, 255)
    color = (color_r, color_g, color_b)
    return color


def draw_dashed_line(initial_pos, length, number, heading):
    my_turtle.setpos(initial_pos)
    my_turtle.setheading(heading)
    for _ in range (0, number):
        my_turtle.forward(length)
        if _ % 2 == 0:
            my_turtle.penup()
        else:
            my_turtle.pendown()


def draw_square(initial_pos, length):
    my_turtle.setpos(initial_pos)
    my_turtle.setheading(0)
    for _ in range(0, 4):
        my_turtle.forward(length)
        my_turtle.right(90)


def draw_polygon(initial_pos, length, num_of_sides):
    my_turtle.setpos(initial_pos)
    my_turtle.setheading(0)
    for _ in range(num_of_sides):
        my_turtle.forward(length)
        my_turtle.right(360/num_of_sides)


def random_walk(initial_pos, length):

    directions = [0, 90, 180, 270]
    my_turtle.setpos(initial_pos)
    my_turtle.setheading(0)
    my_turtle.pensize(10)

    for _ in range(1000):
        my_turtle.color(random_color())
        my_turtle.forward(length)
        my_turtle.setheading(random.choice(directions))


def draw_spirograph(initial_pos, radius, gap_size):
    my_turtle.setpos(initial_pos)
    for _ in range(int(360/gap_size)):
        my_turtle.color(random_color())
        my_turtle.setheading(my_turtle.heading() + gap_size)
        my_turtle.circle(radius)


my_turtle = Turtle()
my_turtle.shape("turtle")
# my_turtle.color("cyan2", "black")
# draw_square(my_turtle.pos(), 100)
# draw_dashed_line(my_turtle.pos(), 20, 10, 180)

# for _ in range(3, 11):
#     turtle.colormode(255)
#     my_turtle.color(random_color())
#     draw_polygon(my_turtle.pos(), 100, _)

my_turtle.speed("fastest")
turtle.colormode(255)
# random_walk(my_turtle.pos(), 25)
draw_spirograph(my_turtle.pos(), 100, 5)

my_screen = Screen()
my_screen.exitonclick()

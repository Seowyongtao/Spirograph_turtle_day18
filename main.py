# from random import random
import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
print(tim)

colours = ["gainsboro", "royal blue", "steel blue", "dark slate gray", "lime green", "olive", "orange", "dark magenta", "hot pink"]
move_direction = [0, 90, 180, 270]


def generate_random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colour = (r, g, b)
    return random_colour

# draw different shapes


# def draw_shape(num_sides):
#
#     tim.color(random.choice(colours))
#
#     degree = 360 / num_sides
#
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(degree)
#
#
# for num in range(3, 11):
#     draw_shape(num)

# random walk

# tim.speed(15)
# tim.pensize(10)
#
#
# def random_walk():
#
#     tim.color(generate_random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(move_direction))
#
#
# for _ in range(0, 100):
#     random_walk()

# drawing spirograph

tim.speed(15)

for _ in range(100):
    tim.color(generate_random_colour())
    tim.circle(100)
    tim.left(5)


myScreen = Screen()
myScreen.exitonclick()



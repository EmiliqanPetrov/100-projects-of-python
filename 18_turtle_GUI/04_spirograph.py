import turtle as t
from random import randint

circle_count = 120

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

for s in range(circle_count):
    tim.color(random_color())
    tim.right(360 / circle_count)
    tim.circle(100)

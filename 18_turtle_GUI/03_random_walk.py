import turtle as t
from random import choice, randint

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.pensize(15)
tim.speed("fast")

while True:
    tim.color(random_color())
    tim.setheading(randint(0, 3) * 90)
    tim.forward(25)

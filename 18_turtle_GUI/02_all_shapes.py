import turtle as t
from random import choice

tim = t.Turtle()
colors = ["red", "orange", "blue", "yellow", "purple", "green"]

tim.forward(100)
tim.left(120)
tim.forward(100)
tim.left(120)
tim.forward(100)
tim.left(120)

for i in range(4, 11):
    tim.color(choice(colors))
    for _ in range(i):
        tim.forward(100)
        tim.left(360 / i)


from random import choice
import turtle as t

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
              (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
              (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
              (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
              (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.dot(15, choice(color_list))
tim.penup()

tim.speed("fast")

for line in range(4):
    for d in range(8):
        tim.forward(30)
        tim.dot(15, choice(color_list))
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.dot(15, choice(color_list))
    for d in range(8):
        tim.forward(30)
        tim.dot(15, choice(color_list))
    if not line == 3:
        tim.right(90)
        tim.forward(30)
        tim.right(90)
        tim.dot(15, choice(color_list))


screen = t.Screen()
screen.exitonclick()

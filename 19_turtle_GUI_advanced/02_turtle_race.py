import turtle as t
import random

is_race_on = False
won = ""
screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a bet", prompt="Which turtle is gonna win: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            won = turtle.color()[0]

        turtle.forward(random.randint(0, 10))

if won == user_bet.lower():
    print("You win!")
else:
    print(f"You lose. It was {won}")

screen.exitonclick()
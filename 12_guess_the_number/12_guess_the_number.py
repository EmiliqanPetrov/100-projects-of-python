import random

RIGHT_ANSWER = "Good job! You guessed it."


def check_number(num):
    if num > number:
        return "Too high"
    elif num < number:
        return "Too low"
    else:
        return "Good job! You guessed it."


print("Welcome to the GUESS THE NUMBER\nI am thinking of a number from 1 to 100")
number = random.randint(1, 100)

difficulty = input("Choice a difficulty: easy('e') or hard('h')")
correct = False

if difficulty == "e":
    count_guess = 10
else:
    count_guess = 5

for _ in range(count_guess):
    guess = int(input(f"Take a guess ({count_guess} guesses left)"))

    print(check_number(guess))
    if check_number(guess) == RIGHT_ANSWER:
        correct = True
        break
    count_guess -= 1

if correct:
    print("You win!")
else:
    print(f"You lose! It was {number}")

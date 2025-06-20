import random
from game_data import data
from art import logo, vs


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    print(f"Current score is {score}")
    print(f"A: {format_data(a_account)}")
    print(vs)
    print(f"B: {format_data(b_account)}")


def end_game():
    print(f"\nYour score is {score}")


a_account = get_random_account()
b_account = get_random_account()
score = 0
flag = True

while flag:
    print("\n" * 20)
    game()

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_answer(user_guess, a_account["follower_count"], b_account["follower_count"]):
        score += 1
        a_account = b_account
        b_account = get_random_account()
    else:
        flag = False
        end_game()

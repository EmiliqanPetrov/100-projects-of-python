import random
from ASCII_art import HANGMAN_PICS
from wordlist import words_list

word = random.choice(words_list)

blanks = ""

for _ in range(len(word)):
    blanks += "-"

print(blanks)

lives = 6
guess = input("Take a guess ").lower()
display = "-" * len(word)
display = list(display)
incorrect_guesses = []

game_over = False
take_life = True

while not game_over:
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            take_life = False

    print("".join(display))

    if (take_life and
            not incorrect_guesses.__contains__(guess) and
            not guess == " "):
        lives -= 1
        incorrect_guesses.append(guess)
        if lives == 0:
            print(HANGMAN_PICS[6])
            print()
            print(f"Game over.\nYou LOSE.\nIt was {word}")
            break
    if word == "".join(display):
        print()
        print("Game over.\nYou WIN.")
        break

    print(HANGMAN_PICS[-(lives + 1)])
    print(f"You have {lives}/6 lives")

    take_life = True
    guess = input("Take a guess ").lower()

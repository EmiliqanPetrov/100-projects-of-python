import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = [random.choice(cards), random.choice(cards)]
computer_cards = [random.choice(cards), random.choice(cards)]
flag = True

while flag:
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if player_score == 21:
        print("\nYou win! BLACKJACK!")
        break
    elif computer_score == 21:
        print("\nYou lose!")
        break
    else:
        if player_score > 21:
            if 11 in player_cards:
                try:
                    index = player_cards.index(11)
                    player_cards[index] = 1
                except ValueError:
                    print("Number not found!")
                player_score = sum(player_cards)
                if player_score > 21:
                    print("\nYou lose!")
                    break
            else:
                print("\nYou lose!")
                break
        else:
            option = input("Do you want another card: 'y' or 'n'")
            if option == "y":
                player_cards.append(random.choice(cards))
            else:
                flag = False
                while computer_score < 17:
                    computer_cards.append(random.choice(cards))
                    computer_score = sum(computer_cards)
                    print(f"Computer cards: {computer_cards}, Computer score: {computer_score}")
                else:
                    print(f"Computer cards: {computer_cards}, Computer score: {computer_score}")
                if computer_score > 21:
                    print("\nYou win!")
                    break
                else:
                    if player_score > computer_score:
                        print("\nYou win!")
                    elif computer_score > player_score:
                        print("\nYou lose!")
                    else:
                        print("\nYou draw!")



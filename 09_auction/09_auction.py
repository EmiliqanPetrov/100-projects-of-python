from ASCII_art import logo

print(logo)

name_price = {}

flag = True

while flag:
    name = input("What is your name: ")
    bid_price = int(input("How much do you wish to bid: $ "))

    name_price[name] = bid_price

    finished = input("Are there more people.Y(es) or N(o): ")
    if finished == "Y":
        flag = True
        print("\n" * 100)
    else:
        flag = False

winner = max(name_price)

print(f"\nSold to {winner}!")

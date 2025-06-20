import data


def print_resources():
    print(f"Water: {data.resources["water"]}")
    print(f"Milk: {data.resources["milk"]}")
    print(f"Coffee: {data.resources["coffee"]}")
    print(f"Money: {data.resources["money"]}")


def check_resources(drink):
    if data.MENU[drink]["ingredients"]["water"] > data.resources["water"]:
        return False
    elif data.MENU[drink]["ingredients"]["milk"] > data.resources["milk"]:
        return False
    elif data.MENU[drink]["ingredients"]["coffee"] > data.resources["coffee"]:
        return False
    else:
        return True


def remove_resources(drink):
    data.resources["water"] -= data.MENU[drink]["ingredients"]["water"]
    data.resources["milk"] -= data.MENU[drink]["ingredients"]["milk"]
    data.resources["coffee"] -= data.MENU[drink]["ingredients"]["coffee"]


def process_coins(drink):
    print(f"The {drink} costs {data.MENU[drink]["cost"]}")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    change = money - data.MENU[drink]["cost"]
    if change >= 0:
        data.resources["money"] += data.MENU[drink]["cost"]
        return f"Here is your {drink}. Your change is {change:.2f}"
    else:
        return f"Sorry, not enough money."


flag = True

while flag:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "espresso":
        if check_resources("espresso"):
            coins = process_coins("espresso")
            print(coins)
            if coins == "Sorry, not enough money.":
                continue
            remove_resources("espresso")
        else:
            print("Sorry, not enough resources.")

        continue
    elif user_input == "latte":
        if check_resources("latte"):
            coins = process_coins("latte")
            print(coins)
            if coins == "Sorry, not enough money.":
                continue
            remove_resources("latte")
        else:
            print("Sorry, not enough resources.")

        continue
    elif user_input == "cappuccino":
        if check_resources("cappuccino"):
            coins = process_coins("cappuccino")
            print(coins)
            if coins == "Sorry, not enough money.":
                continue
            remove_resources("cappuccino")
        else:
            print("Sorry, not enough resources.")

        continue
    elif user_input == "off":
        print(f"You made {data.resources["money"]:.2f} dollars.")
        flag = False
    elif user_input == "report":
        print_resources()
        continue

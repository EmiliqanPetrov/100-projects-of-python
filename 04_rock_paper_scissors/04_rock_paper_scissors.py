import random

print("What do you choose? Type: 0 - rock; 1 - paper; 2 - scissors")

possibilities = ["rock", "paper", "scissors"]

player = possibilities[int(input())]
print(f"You chose {player}")
if player == "rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif player == "paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif player == "scissors":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
computer = random.choice(possibilities)
print(f"Bot chose {computer}")
if computer == "rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer == "paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif computer == "scissors":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if player == computer:
    print("It's a draw!")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
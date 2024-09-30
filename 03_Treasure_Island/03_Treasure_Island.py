import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
time.sleep(2)
print("Welcome to Treasure Island.")
time.sleep(1)
print("Your mission is to find the treasure.")
time.sleep(1)

des1 = input("You are in a mine and there are two tunnels(right and left).What direction do you go in.\n")
time.sleep(1)

if des1.lower() == "left":
    des2 = input("You get out of the cave but now you are stranded\n"
                 "on the neighbor island of the island with the treasure.\n"
                 "Do you swim to the other island or do you wait.\n")
    time.sleep(1)
    if des2.lower() == "wait":
        des3 = input("When it gets dark outside you see a campfire and you go there.From there you see a house\n"
                     "with a note that says 'Dear pirate, you have found the treasure.\n"
                     "It is in one of the three entrances.'You see a red door, a blue door,and a yellow door.\n"
                     "Which door do you chose.\n")
        time.sleep(1)
        if des3.lower() == "yellow":
            print("Congratulations! You win!")
        elif des3.lower() == "red":
            print("In there is an old tribe. They attack you with their spears.\nGame over.")
        else:
            print("You see a lion. It attacks you.\nGame over.")
    else:
        print("You were eaten by a big shark.\nGame over.")
else:
    print("You fall into a deer trap.\nGame over.")

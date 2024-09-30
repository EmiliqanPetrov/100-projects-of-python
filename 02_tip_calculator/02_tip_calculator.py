import time

print("Welcome to the tip calculator!")
time.sleep(2)
price = float(input("What was the total bill? $"))
time.sleep(2)
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
time.sleep(2)
people_count = int(input("How many people to split the bill? "))
time.sleep(2)

money = (price + price * tip_percent) / people_count

print(f"Each person should pay: ${money:.2f}")
import sys

numbers = [17, 36, 1, 42, 25, 83, 89, 26, 84, 80, 27, 79, 73, 35, 95]

max_number = -sys.maxsize

for i in range(0, len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]

print(max_number)
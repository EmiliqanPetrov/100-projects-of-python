import ascii_art


def add(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def do_opps():
    if operation == "+":
        return add(cur_num1, cur_num2)
    elif operation == "-":
        return minus(cur_num1, cur_num2)
    elif operation == "*":
        return multiply(cur_num1, cur_num2)
    elif operation == "/":
        return divide(cur_num1, cur_num2)


print(ascii_art.logo)
result = 0
cur_num1 = int(input("First number - "))
operation = input("Choice of operation\n+\n-\n*\n/\n")
cur_num2 = int(input("Second number - "))

result = do_opps()

print(f"The result is {result}")
flag = input("Do you want to continue calculating with the result? 'y' or 'n' ")

while flag == "y":
    cur_num1 = result
    operation = input("Choice of operation\n+\n-\n*\n/\n")
    cur_num2 = int(input("Second number - "))

    result = do_opps()

    print(f"The result is {result}")

    flag = input("Do you want to continue calculating with the result? 'y' or 'n' ")

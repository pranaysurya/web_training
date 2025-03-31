print("Add")
print("Subtract")
print("Multiply")
print("Divide")


sel = input("Choose your option:")

number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))


def add(number1, number2):
    print("Sum of", number1, "+", number2, "=", number1 + number2)


def subtract(number1, number2):
    print("Difference of", number1, "-", number2, "=", number1 - number2)


def multiply(number1, number2):
    print("Product of", number1, "*", number2, "=", number1 * number2)


def divide(number1, number2):
    print("Division of", number1, "/", number2, "=", number1 / number2)


if sel == "Add":
    add(number1, number2)
elif sel == "Subtract":
    subtract(number1, number2)
elif sel == "Multiply":
    multiply(number1, number2)
elif sel == "Divide":
    divide(number1, number2)
else:
    print("invalid option")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

running = True


def select():
    global running
    sel = input("Choose your option:")

    if len(str(sel)) == 1:

        if 0 < sel < 6:

            if sel != 5:

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

                if sel == 1:
                    add(number1, number2)
                elif sel == 2:
                    subtract(number1, number2)
                elif sel == 3:
                    multiply(number1, number2)
                elif sel == 4:
                    divide(number1, number2)

            else:
                print("Exiting calculator. Goodbye!")
                running = False

        else:
            print("invalid option")
            select()

    else:
        operations_array = str(sel).split(" ")
        print(operations_array)

while running:
    select()
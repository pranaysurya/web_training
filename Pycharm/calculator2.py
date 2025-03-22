print("Choose an operation:")

print("1. Addition")

print("2. Subtraction")

print("3. Multiplication")

print("4. Division")

print("5. Exit")

running = True


def calculate(val):
    global running
    print ("\n")

    if 6 > val > 0:
        num1 = float(input("Enter your first number: "))

        num2 = float(input("Enter your second number: "))

        if val == 1:
            print (str(float(num1)) + " plus " + str(float(num2)) + " is equal to " + str(float(num1) + float(num2)) + "\n")

        elif val == 2:
            print (str(float(num1)) + " minus " + str(float(num2)) + " is equal to " + str(
                float(num1) - float(num2)) + "\n")

        elif val == 3:
            print (str(float(num1)) + " times " + str(float(num2)) + " is equal to " + str(
                float(num1) * float(num2)) + "\n")

        elif val == 4:
            print (str(float(num1)) + " divided by " + str(float(num2)) + " is equal to " + str(
                float(num1) / float(num2)) + "\n")

        elif val == 5:
            print ("\n")
            print ("Exiting the calculator. Goodbye!")
            running = False

    else:
        print ("That is not one of the options.")

        select()


def select():
    global running

    choice = input("Enter your corresponding choice (1-5): ")

    if choice == 5:
        print ("\n")
        print ("Exiting the calculator. Goodbye!")
        running = False

    else:
        calculate(int(choice))


while running:
    select()

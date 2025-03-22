def call():
    
    x = int(input("Enter a number:"))

    if int(x) % 2 == 0:
        print(str(x) + " is even.")

    elif int(x) % 2 != 0:
        print(str(x) + " is odd.")


while True:
    call()
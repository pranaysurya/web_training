try:
    i = int(input("Enter number: "))
    b = int(input("Enter another number: "))

    if i < b:
        print ("hello")
    
except Exception as e:
    print ("The given input was not a number.", e)  


try:
    if i % 2 == 0:
        print ("even")
    
    else:
        print("Odd")

except Exception as e:
    print("The number was not a whole number", e)
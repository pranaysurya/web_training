class Parent():
    global v1
    v1 = int(input("Enter a number from 1-10: "))

    def mathing(self, val1, val2, val3):
        if val1 < 5:
            print("{} is less than 5.".format(val1))

        elif val1 > 5:
            print("{} times {} is {}.".format(val1, val2, val1*val2))



class Child(Parent):

    def __init__(self):
        print("Goodbye!")

e = Child()

e.mathing(v1, 32, 64)
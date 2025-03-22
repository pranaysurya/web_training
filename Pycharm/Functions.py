"""
def check(x):
    if x % 2 == 0:
        print (str(x) + " is even.")

    else:
        print (str(x) + " is odd.")


def sum(a, b):
    print (str(a) + " plus " + str(b) + " is equal to " + str(a + b))


y = input("Enter an integer to check if it is even or odd:")

check(y)

num1 = input("Enter your first integer to add:")
num2 = input("Enter your second integer to add:")
sum(num1, num2)


def myFun(d, s=50):
    print(d + s)


myFun(234)


def addon(*first_name):
    print (first_name)


addon("Pranay", "Hello")
addon("Dad")



def name(**v1):
    print (v1)
    print (v1["v4"])


name(v1=1, v2=2, v3=3, v4=4, v5=5, v6=6)
"""


def cases(**values):
    print("fname: " + values["fname"])
    print("lname: " + values["lname"])
    print("address: " + values["address"] + "\n")

print ("case1:")
cases(fname="Pranay", lname="Addagarla", address="Canada")

print ("case2:")
cases(fname="Jack", lname="Sparrow", address="Carribeans")

# Python program to
# demonstrate accessing of
# variables of nested functions


global s
def f1():
    s = 'I lovs coding'
    f2(s)

def f2(value):
    print(value)




# Driver's code
f1()
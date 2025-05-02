#
# square = lambda a : a ** 2
#
# square_root = lambda b : b ** 0.5
#
# even_or_odd = lambda x : "Even" if x % 2 == 0 else "Odd"
#
# y = input("Enter number to square: ")
#
# print(square(y))
#
# z = input("Enter number to square root: ")
#
# print(square_root(z))
#
# q = input('Enter a number to see if it is even or odd: ')
#
# print(even_or_odd(q))
#
# cube = lambda a : a ** 3
#
# y = input("Enter a number to cube and cube root: ")
#
# print(cube(y))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 90, 12, 41, 243, 4, 12214]

for i in numbers:
    message = lambda : i
    # print(message()) if i % 2 == 0 else ""
    count = []
    count.append(i) if i % 2 == 0 else ""
    print(count)
    if count[i] != "":
        v = [count]
    else:
        count.remove(i)

print (v)
# print(numbers)
# print(i)
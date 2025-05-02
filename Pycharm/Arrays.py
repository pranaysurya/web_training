import array as arr

a = arr.array("i", [1, 2, 3])

print(a)

b = arr.array("u", "Bat")

print(b)

c = arr.array("d", [1.1, 2.2, 3.3])

# print(c[1])

# print(c[2])

# print(c[0])


print(c)
c.insert(0, 3.2)

count = 0

while  count < len(c):

    print(c[count])

    if count == len(c):
        break

    count += 1
    

for loc, val in enumerate(c):
    print(f"Index: {loc} Value: {val} ")


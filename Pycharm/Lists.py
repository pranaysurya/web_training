x = 1
y = "Hello"
z = True

h = [x,y,z]
q = [31, "Hi", True, False, 2.43, h]
print (h)
print (q)

print (type(q))
print (len(q))

print(q[1:5])
print(q[-4:-2])

q[3] = "World"

print (q)

h[2:3] = "Hello", 1, 3.9j

print (h)

q.insert(2, "Haha!")
print (q)

q.append("New Value Added")
print (q)

a = [1, 2, 34, 5, 5, 5, 5]
b = ["One", "Two", "Three", "Four"]
a.extend(b)
print (a)

a.remove(5)
print (a)

a.pop(2)
print (a)

# a.clear()
# print (a)

d = [1, 5, 6, 7, 8, 22, 343, 12321, 231423, 23, 45, 54, 2984, 3892, 34783]
d.sort()

print (d)
d.sort(reverse=True)

print (d)

# del a
# print (a)


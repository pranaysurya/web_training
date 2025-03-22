s = [10, 9, 2.5, True]


# for i in range(5):
#     print (i)
#
# for i in range(2, 20, 4):
#     print (i)

q = ["Hello", "Hi", "Good Morning"]

for i in range(len(q)):
    if i < (len(q) - 1):
        print (q[i])
    else:
        break

# w = [1, 2, 3, 4, 5, 6]
#
# for i in w:
#     if i % 2 != 0:
#         print (i)
#
# W = (1, -2, 3, -5)
#
# for i in W:
#     if i > 0:
#         print (i)
#
#
# for i in W:
#     if i < 0:
#         print (i)
#
# x = [101, 727, 968, 324, 1012]
# v = x[0]
#
# for i in x:
#     if i > v:
#         v = i
#
# x.remove(int(v))
# y = x[0]
#
# for i in x:
#     if i > y:
#         y = i
#
# print (y)

q = "Hello World"
count = set()
res = ""

for i in q:
    if i not in count:
        count.add(i)
        res += i

print (res)




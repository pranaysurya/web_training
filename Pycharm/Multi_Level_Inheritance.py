class Add():

    def add(self, x, y):
        return x + y
    
class Subtract(Add):
    
    def subtract(self, x, y):
        return x - y

class Calc(Subtract):

    def double(self, x, y):
        return 2 * (x + y)

q = Calc()

v1 = 7
v2 = 3

print(q.add(v1, v2))

print(q.subtract(v1, v2))

print(q.double(v1, v2))

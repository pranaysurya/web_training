# class Employee:
#     def sound(self):
#         return "23"
# class John(Employee):
#     def sound(self):
#         return "48"
# class Hilda(Employee):
#     def sound(self):
#         return "67"
# # Polymorphic behavior
# emplyees = [John(), Hilda(), Employee()]
# for animal in emplyees:
#     print(animal.sound())  # Calls the overridden method based on the object type   

class Employee:
    def __init__(self, h):
        self.value = h
        print("Hello",self.value)
    def sound(self, x):
     self.value1 = x
     print(f"{self.value1}")
class John(Employee):
    def sound(self, x):
        self.value1 = x
        print(f"{self.value1}")
    def __init__(self, h):
        print(f"Hello {h}")
class Hilda(John):
        def sound(self, x):
         self.value1 = x
         print(f"{self.value1}")
# Polymorphic behavior
emplyees = [Hilda(" World"), John(50),Employee("hi")]
for animal in emplyees:
    print(animal.sound("78"))  # Calls the overridden method based on the object type

class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")
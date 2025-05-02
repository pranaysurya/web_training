import math

radius = input("Enter a radius for a circle: ")

circumference = 2 * math.pi * float(radius)

area = math.pi * (float(radius) ** 2)

print(f"The circumference of the circle is {circumference} and the area is {area}.")
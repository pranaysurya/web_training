class Calculator:

    def add(self, a,b):
        return a + b
    
    def subtract(self,a,b):
        return a - b
    
    def multiply(self,a,b):
        return a * b
    
    def divide(self, a,b):
        return a / b
    
x = 2
y = 3

z = Calculator()

print(z.add(x,y))

print(z.subtract(x,y))

print(z.multiply(x,y))

print(z.divide(x,y))

class Printing():

    def printer(self, val):
        print(val)



val1 = input("Enter a value:")

p = Printing()

w = Printing()

p.printer(val1)

w.printer(val1)


# class EmployeeBasing():

#     def employmentinfo(self, name, age, salary):
#         print("Name: {}.".format(name))
#         print("Age: {}.".format(age))
#         print("Salary: {}.".format(salary))
        

# Employer = EmployeeBasing()

# y = EmployeeBasing()

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# salary = input("Enter your salary: ")


# name1 = input("Enter your name: ")
# age1 = input("Enter your age: ")
# salary1 = input("Enter your salary: ")

# Employer.employmentinfo(name, age, salary)

# y.employmentinfo(name1, age1, salary1)
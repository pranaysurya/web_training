# Encapsulation in Python
# # public
# class Public:
#     def __init__(self):
#         self.name = "John"  # Public attribute
#     def display_name(self):
#         print(self.name)  # Public method
# obj = Public()
# obj.display_name()  # Accessible
# print(obj.name)  # Accessible

# Encapsulation in Python
# public
# class Public:
#     def __init__(self):
#         self.__name = "John"  # Public attribute
#     def __display_name(self):
#         return self.__name  # Private method
# obj = Public()
# obj.display_name()  # Accessible
# print(obj.__name)  # Accessible



class Hello():

    def __init__(self):
        print("Hello World")

class Hi(Hello):

    def new(self):
        self.value = __name
        __name = "Jack"

        return __name
    
    def rewrite(self):
        print(new())


o = Hi()

print(o.new())

print(o.rewrite())

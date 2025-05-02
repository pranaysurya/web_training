class School:
    
    def roll_call(self, namelist):
        c = 1
        for i in list(namelist):
            print("{}. ".format(c) + i)
            c += 1


    def score(self, test_values):
        v = 1  
        for i in test_values:

            if 80 < i < 90:
                print("Role Number {} -> ".format(v) + "A")

            elif 70 < i < 80:
                print("Role Number {} -> ".format(v) + "B") 

            elif 60 < i < 70:
                print("Role Number {} -> ".format(v) + "c")  

            elif 50 < i < 60:
                print("Role Number {} -> ".format(v) + "D")  
            
            v += 1


students = ["Sam", "John", "Robert", "Pranay", "Jad", "Ryan", "Ady", "Val", "Rick", "Jacob"]

marks = [78, 91, 83, 97, 82, 64, 98, 77, 62, 58]
e = School()

e.roll_call(students)

e.score(marks)
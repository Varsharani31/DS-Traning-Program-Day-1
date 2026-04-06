# WAP for Multiple Inheritance

class subjMarks:                                        # Parent Class 1
    math = int(input("Enter marks in Math : "))
    DE = int(input("Enter marks in DE : "))
    C = int(input("Enter marks in C : "))
    english = int(input("Enter marks in English : "))

class PractMarks:                                       # Parent Class 2
    cprac = int(input("Enter marks in C prac : "))

class Result(subjMarks, PractMarks):                    # Child Class
    def total(self):
        if self.math >= 40 and self.DE >= 40 and self.C >= 40 and self.english >= 40 and self.cprac >= 40:
            print("Pass")
        else:
            print("Fail")

obj = Result()                                          # Creating Object
obj.total()                                             # Calling Method


# Output =
# Enter marks in Math : 60
# Enter marks in DE : 50
# Enter marks in C : 60
# Enter marks in English : 70
# Enter marks in C prac : 50
# Pass
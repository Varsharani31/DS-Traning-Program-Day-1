# WAP to understand why directly method overloading not supported in python.
# Function name is same but it takes different number of arguments.
# Python does not support method overloading directly and constructor overloading also.
# Python support Operator Overloading and Function Overloading.


class Arithmatic:  
    def add(self,a):  
        print(a)  
    def add(self,a,b):  
        print(a+b)  
    def add(self,a,b,c):  
        print(a+b+c)  
obj = Arithmatic()  
obj.add(10)  
obj.add(10,20)  
obj.add(1,2,3)

# Output = 
# Traceback (most recent call last):
#   File "e:\DS Training Program\Day 5\Prg19_Method_Overloading.py", line 11, in <module>
#     obj.add(10)
#     ~~~~~~~^^^^
# TypeError: Arithmatic.add() missing 2 required positional arguments: 'b' and 'c'
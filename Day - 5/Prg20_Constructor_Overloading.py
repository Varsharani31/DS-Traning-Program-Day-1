# WAP for constructor overloading

# Constructor Overloading is not supported in python directly.

class Arithmetic:
    def __init__(self):
        print("There is no argument")
    def __init__(self,a):
        print("Passing 1 argument")
    def __init__(self,a,b):
        print("Passing 2 argument")
   
obj = Arithmetic()
obj.add(10)
obj.add(10,20)



# Output = 
# Traceback (most recent call last):
#   File "e:\DS Training Program\Day 5\Prg20_Constructor_Overloading.py", line 13, in <module>
#     obj = Arithmetic()
# TypeError: Arithmetic.__init__() missing 2 required positional arguments: 'a' and 'b'





# We can handle constructor overloading by using default arguments.

class Arithmatic:  
    def __init__(self,a=None,b=None,c=None):  
        if a!=None and b!=None and c!=None:
            print(a+b)
        elif a!=None and b!=None:
            print(a+b+c)
        else:
            print("Enter Atleast 2 Argument")  
obj = Arithmatic()  
obj.add(10)  
obj.add(10,20)  
obj.add(1,2,3)


# Output =
# Enter Atleast 2 Argument  
# 30
# 6
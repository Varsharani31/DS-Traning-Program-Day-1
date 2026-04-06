# WAP to handle method overloading in python.

class Arithmatic:  
    def add(self,a=None,b=None,c=None):  
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
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
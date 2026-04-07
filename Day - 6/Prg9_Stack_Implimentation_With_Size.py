# Stack Implimentation : Stack Implimentation with size limit


import sys 


class Stack:
    def __init__(self,stackSize):       # Parameterized Constructor
       self.stackList = []              # Stack is Created
       self.size = stackSize

    def Push(self,value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.stackList.append(value)

    def Pop(self):
        if self.IsEmpty():
            return "Stack is Empty"
        else:
            return self.stackList.pop()

    def IsEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False
    
    def deleteStack(self):
        self.stackList = None
        return "Stack is Deleted"

    def Display(Stack):
        print("----------------------------")
        print(Stack.stackList)
        print("----------------------------")

    
    def Peek(self):
        if self.IsEmpty():
            return "Stack is Empty"
        else:
            return self.stackList[-1]

    def isFull(self):
        if len(self.stackList) == self.size:
            return True
        else:
            return False

stackSize = int(input("Enter the size of the stack : "))   
stackObj = Stack(stackSize)

while True:
    print("1. PUSH Element is Stack")
    print("2. POP Element is Stack")
    print("3. Check Is the Stack Is EMPTY")
    print("4. DELETE Stack")
    print("5. DISPLAY Stack Elements")
    print("6. PEEK")
    print("7. Check Is the Stack Is FULL")
    print("8. EXIT")

    choice = int(input("Enter your choice : "))

 
    if choice == 1:
        val = int(input("Enter element for stack : "))
        result = stackObj.Push(val)
        if result:
            print(result)

    elif choice == 2:
        print(stackObj.Pop())

    elif choice == 3:
        print(stackObj.IsEmpty())

    elif choice == 4:
        print(stackObj.deleteStack())

    elif choice == 5:
        stackObj.Display()

    elif choice == 6:
        print(stackObj.Peek())

    elif choice == 7:
        print(stackObj.isFull())
    
    elif choice == 8:
        sys.exit()

    else:
        print("Invalid choice")
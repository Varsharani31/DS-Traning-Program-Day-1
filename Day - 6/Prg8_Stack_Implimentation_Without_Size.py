# Stack Implimentation : Stack Implimentation without size limit


import sys 


class Stack:
    def __init__(self):
       self.stackList = []              # Stack is Created
        
    def Push(self,value):
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

    def Peek(self):
        if self.IsEmpty():
            return "Stack is Empty"
        else:
            return self.stackList[-1]

    def Display(Stack):
        print("----------------------------")
        print(Stack.stackList)
        print("----------------------------")

    
stackObj = Stack()

while True:
    print("1. PUSH Element is Stack")
    print("2. POP Element is Stack")
    print("3. Check Is the Stack Is EMPTY")
    print("4. DELETE Stack")
    print("5. DISPLAY Stack Elements")
    print("6. PEEK")
    print("7. EXIT")

    choice = int(input("Enter your choice : "))

 
    if choice == 1:
        val = int(input("Enter element for stack : "))
        stackObj.Push(val)

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
        sys.exit()

    else:
        print("Invalid choice")



# Output =
# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 1
# Enter element for stack : 11

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 1
# Enter element for stack : 31

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 1
# Enter element for stack : 7

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 2
# 7

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 3
# False

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 5
# ----------------------------
# [11, 31]
# ----------------------------

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 6
# 31

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 4
# Stack is Deleted

# 1. PUSH Element is Stack
# 2. POP Element is Stack
# 3. Check Is the Stack Is EMPTY
# 4. DELETE Stack
# 5. DISPLAY Stack Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 7
# PS E:\DS Training Program>
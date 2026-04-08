# WAP to implement a queue without size limit.

import sys 

class Queue:
    def __init__(self):       
       self.queueList = []              # Queue is Created

    def Enqueue(self,value):
        if self.queueList is None:
            return "Queue is Deleted"
        else:
            self.queueList.append(value)
            return "Element Enqueued"

    def Dequeue(self):
        if self.queueList is None:
            return "Queue is Deleted"
        elif self.IsEmpty():
            return "Queue is Empty"
        else:
            return self.queueList.pop(0)

    def IsEmpty(self):
        if self.queueList == []:
            return True
        else:
            return False
    
    def deleteQueue(self):
        self.queueList = None
        return "Queue is Deleted"

    def Display(Queue):
        print("----------------------------")
        print(Queue.queueList)
        print("----------------------------")

    
    def Peek(self):
        if self.IsEmpty():
            return "Queue is Empty"
        else:
            return self.queueList[0]
  
queueObj = Queue()

while True:
    print("1. ENQUEUE Element is Queue")
    print("2. DEQUEUE Element is Queue")
    print("3. Check Is the Queue Is EMPTY")
    print("4. DELETE Queue")
    print("5. DISPLAY Queue Elements")
    print("6. PEEK")
    print("7. EXIT")

    choice = int(input("Enter your choice : "))

 
    if choice == 1:
        val = int(input("Enter element for queue : "))
        result = queueObj.Enqueue(val)
        if result:
            print(result)

    elif choice == 2:
        print(queueObj.Dequeue())

    elif choice == 3:
        print(queueObj.IsEmpty())

    elif choice == 4:
        print(queueObj.deleteQueue())

    elif choice == 5:
        queueObj.Display()

    elif choice == 6:
        print(queueObj.Peek())
    
    elif choice == 7:
        sys.exit()

    else:
        print("Invalid choice")



# Output = 
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 1
# Enter element for queue : 11
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 1
# Enter element for queue : 31
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 3
# False
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 5
# ----------------------------
# [11, 31]
# ----------------------------
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 2
# 11
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 5
# ----------------------------
# [31]
# ----------------------------
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 6
# 31
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 4
# Queue is Deleted
# 1. ENQUEUE Element is Queue
# 2. DEQUEUE Element is Queue
# 3. Check Is the Queue Is EMPTY
# 4. DELETE Queue
# 5. DISPLAY Queue Elements
# 6. PEEK
# 7. EXIT
# Enter your choice : 7
# PS E:\DS Training Program> 
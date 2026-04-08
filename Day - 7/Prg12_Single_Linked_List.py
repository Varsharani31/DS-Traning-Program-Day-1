# WAP for Single Linked List
import sys

class Node:
    def __init__(self,data):
        self.data = data                                    # Instance Variable
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Add Node

    def addNode(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Add Node At Beginning

    def addNodeAtBeginning(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    # Add Node In Between

    def addNodeInBetween(self, value, target_data):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
            
        temp = self.head
        while temp is not None:
            if temp.data == target_data:
                node.next = temp.next
                temp.next = node
                if node.next is None:
                    self.tail = node
                return
            temp = temp.next
            
        print("Target node not found.")

    # Add Node At End

    def addNodeAtEnd(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Display Linked List

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " ----> ")
            temp = temp.next
        print("None")
    
if __name__ == "__main__":
    object = LinkedList()

    while True:
        print('1. Add Node In Linked List')
        print('2. Add Node At Beginning')
        print('3. Add Node In Between')
        print('4. Add Node At End')
        print('5. Display Linked List')
        print('6. Exit')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the data: "))
            object.addNode(value)
            print("Node added successfully")

        elif choice == 2:
            value = int(input("Enter the data: "))
            object.addNodeAtBeginning(value)
            print("Node added successfully")

        elif choice == 3:
            value = int(input("Enter the data for the new node: "))
            target_data = int(input("Enter the data of the existing node after which you want to insert: "))
            object.addNodeInBetween(value, target_data)
            print("Node added successfully")

        elif choice == 4:
            value = int(input("Enter the data: "))
            object.addNodeAtEnd(value)
            print("Node added successfully")

        elif choice == 5:
            object.display()

        elif choice == 6:
            break
        else:
            print("Invalid choice")



# Output = 
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 1 
# Enter the data: 11
# Node added successfully
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 1
# Enter the data: 31
# Node added successfully
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 5
# 11 ----> 31 ----> None
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 2
# Enter the data: 7
# Node added successfully
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 5
# 7 ----> 11 ----> 31 ----> None
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 3
# Enter the data for the new node: 2
# Enter the data of the existing node after which you want to insert: 11
# Node added successfully
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 5
# 7 ----> 11 ----> 2 ----> 31 ----> None
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 4 
# Enter the data: 5
# Node added successfully
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 5
# 7 ----> 11 ----> 2 ----> 31 ----> 5 ----> None
# 1. Add Node In Linked List
# 2. Add Node At Beginning
# 3. Add Node In Between
# 4. Add Node At End
# 5. Display Linked List
# 6. Exit
# Enter your choice: 6
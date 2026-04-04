# WAP for Menu Driven Code

import sys                                             
def add():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    return num1 + num2

def sub():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    return num1 - num2

def mul():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    return num1 * num2

def div():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    return num1 / num2

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter Your choice : "))

    if choice == 1:
        print("Addition : ",add())
    elif choice == 2:
        print("Subtraction : ",sub())
    elif choice == 3:
        print("Multiplication : ",mul())
    elif choice == 4:
        print("Division : ",div())
    elif choice == 5:
        sys.exit()
    

# Output = 
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter Your choice : 1
# Enter First Number : 11
# Enter Second Number : 31
# Addition :  42


# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter Your choice : 2
# Enter First Number : 31
# Enter Second Number : 11
# Subtraction :  20


# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter Your choice : 3
# Enter First Number : 11
# Enter Second Number : 31
# Multiplication :  341


# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter Your choice : 4
# Enter First Number : 11
# Enter Second Number : 31
# Division :  0.3548387096774194


# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter Your choice : 5
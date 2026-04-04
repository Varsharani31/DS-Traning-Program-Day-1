# Q.1

n = int(input("Enter no. of rows : "))
for i in range(1,n+1):                            # Outer Loop => Row's
    for j in range(1,1+i):                        # Inner Loop => Col's
        print(j, end = " ")
    print()

# Output = Enter no. of rows : 5
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# Q.2

n = int(input("Enter no. of rows : "))
for i in range(1,n+1):                            # Outer Loop => Row's
    for j in range(1,1+i):                        # Inner Loop => Col's
        print(chr(64+i), end = " ")
    print()

# Output = Enter no. of rows : 5
# A 
# B B
# C C C
# D D D D
# E E E E E


# Q.3

n = int(input("Enter no. of rows : "))
for i in range(1,n+1):                            # Outer Loop => Row's
    for j in range(1,n+2-i):                      # Inner Loop => Col's
        print("*", end = " ")
    print()

# Output = Enter no. of rows : 5
# * * * * * 
# * * * *
# * * *
# * *
# *


# Q.4

import time
n = int(input("Enter no. of rows : "))
for i in range(1,n+1):                            # Outer Loop => Row's
    for j in range(1,n+2-i):                      # Inner Loop => Col's
        time.sleep(2)                             # wait for 2 sec before printing each row
        print(chr(64+j), end = " ")
    print()

# Output = Enter no. of rows : 5
# A B C D E 
# A B C D
# A B C
# A B
# A


# Q.5

import time
n = int(input("Enter no. of rows : "))
for i in range(1,n+1):                            # Outer Loop => Row's
    for j in range(1,n+2-i):                      # Inner Loop => Col's
        time.sleep(2)                             # wait for 2 sec before printing each row
        print(n+1-i, end = " ")
    print()

# Output = Enter no. of rows : 5
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 


# Q.6

import time
n = int(input("Enter no. of rows : "))
for i in range(1,n+1):
    print(" " * (n-i),end = " ")                            # Outer Loop => Row's
    for j in range(1,n+2-i):                                # Inner Loop => Col's
        time.sleep(2)                                       # wait for 2 sec before printing each row
        print("*", end = " ")
    print()

# Output = Enter no. of rows : 5
#      * * * * * 
#     * * * * 
#    * * * 
#   * * 
#  * 
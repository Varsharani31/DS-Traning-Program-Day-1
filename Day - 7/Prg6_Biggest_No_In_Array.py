# WAP to find the biggest number in an array.

arr = [11,31,2,7,5]

def findBiggest(arr):
    biggest = arr[0]                                            # Time Complexity : O(1)
    for i in range(1,len(arr)):                                 # Time Complexity : O(n)
        if arr[i] > biggest:                                    # Time Complexity : O(1)
            biggest = arr[i]                                    # Time Complexity : O(1)
    return biggest                                              # Time Complexity : O(1)

print("Biggest element is : ",findBiggest(arr))                 # Time Complexity : O(1)


# Output = 
# Biggest element is :  31
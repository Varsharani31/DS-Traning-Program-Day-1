# WAP to check element in the array using linear search algorithm

array = [1,2,3,4,5,6,7,8,9]
target = 4

def linearSearch(array,target):                                             # Time Complexity = O(1)
    for i in range(len(array)):                                             # Time Complexity = O(n)
        if array[i] == target:                                              # Time Complexity = O(1)
            return i                                                        # Time Complexity = O(1)
    return -1                                                               # Time Complexity = O(1)

result = linearSearch(array,target)                                         

if result != -1:                                                            
    print("Element found at index",result)                                  
else:
    print("Element not found")                                              


# Output = 
# Element found at index 3
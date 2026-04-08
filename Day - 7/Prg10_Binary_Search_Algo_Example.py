# WAP Binary Search Algorithm

def binarySearch(array, target):                            #Time Complexity = O(1)
    low = 0                                                 #Time Complexity = O(1)
    high = len(array) - 1                                   #Time Complexity = O(1)

    while low <= high:                                      #Time Complexity = O(log n)
        mid = (low + high) // 2                             #Time Complexity = O(1)

        if array[mid] == target:                            #Time Complexity = O(1)
            return mid                                      #Time Complexity = O(1)

        elif array[mid] < target:                           #Time Complexity = O(1)
            low = mid + 1                                   #Time Complexity = O(1)

        else:                                               #Time Complexity = O(1)
            high = mid - 1                                  #Time Complexity = O(1)

    return -1                                               #Time Complexity = O(1)


array = [1,2,3,4,5,6,7,8,9]
target = 4
result = binarySearch(array, target)                        #Time Complexity = O(log n)

if result != -1:                                            #Time Complexity = O(1)
    print("Element found at index", result)                 #Time Complexity = O(1)
else:
    print("Element not found")                              #Time Complexity = O(1)



# Output = Element found at index 3
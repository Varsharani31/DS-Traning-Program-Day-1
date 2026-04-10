# WAP to capitalize the first letter of each word in a string using recursion.

def capitalize_first_letter(arr):
    
    result = []
    if len(arr) == 0:
        return result
   
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalize_first_letter(arr[1:])

print(capitalize_first_letter(["car","taco","banana"]))  



# Output = ['Car', 'Taco', 'Banana']
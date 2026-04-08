# WAP to find the square plot of a given area

n = int(input("Enter the number : "))
areas = list(map(int, input("Enter the areas : ").split()))

count = 0

for num in areas:
    i = 1
    while i * i <= num:
        if i * i == num:
            count += 1
            break
        i += 1

print(count)    


# Output = 
# Enter the number : 8
# Enter the areas : 79 77 54 81 48 34 25 16
# 3
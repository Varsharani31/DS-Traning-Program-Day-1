# WAP to calculate majority element

a = [3,3,4,2,4,4,2,4,4]
candidate = None
count = 0
for num in a:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
print(candidate)                                        # Output = 4
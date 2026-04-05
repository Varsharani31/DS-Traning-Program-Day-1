# WAP to remove all occarance of element from list output = [1,3,4]

my_list = [1, 2, 2, 3, 4, 2]

result = []
for item in my_list:
    if my_list.count(item) <= 2:
        result.append(item)
print(result)


# Output = [1, 3, 4]

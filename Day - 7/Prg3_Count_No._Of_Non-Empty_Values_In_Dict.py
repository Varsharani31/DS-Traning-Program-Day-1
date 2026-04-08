# WAP to count the number of non-empty values in a dictionary.

dict1 = {"A":1,"B":"","C":"3","D":None,"E":5}
print(dict1)
d = []
count = 0

for i in dict1.items():
    if i[1] != "" and i[1] != None:
        count += 1
print(count)


# Output =
# {'A': 1, 'B': '', 'C': '3', 'D': None, 'E': 5}
# 3
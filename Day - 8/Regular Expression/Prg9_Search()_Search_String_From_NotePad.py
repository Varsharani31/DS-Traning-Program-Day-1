# WAP to search the pattern in the string using search() method of regular expression by taking input from the user

import re

pattern = input("Enter the pattern to perform search operation : ")

f = open("File.txt", "r")
content = f.read()

matcher = re.search(pattern, content)
print(matcher)

if matcher != None:
    print("Pattern found")
    print(matcher.start(),"......",matcher.end())
else:
    print("Pattern not found")


# Output = 
# Enter the pattern to perform search operation : Function
# <re.Match object; span=(0, 8), match='Function'>
# Pattern found
# 0 ...... 8

# Enter the pattern to perform search operation : is
# <re.Match object; span=(1, 3), match='is'>
# Pattern found
# 1 ...... 3
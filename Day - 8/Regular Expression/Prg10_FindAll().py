# WAP using findall() method of regular expression

# findall method return a list which containing all matches.

import re
pattern = re.findall('[0-9]',"abch3hdh5bk7ZQ$&*")
print(pattern)


# Output = 
# ['3', '5', '7']
# WAP using subn() method of regular expression

# subn() it is similer to sub() method but it return a tuple where 1st element is the new string and 2nd element is the number of substitution.

import re
pattern = re.subn('[1-9]','*','1131 Rani Manas')
print(pattern)
print("The String is : ",pattern[0])
print("The Number of Substitution is : ",pattern[1])


# Output = 
# The String is :  **** Rani Manas
# The Number of Substitution is :  4
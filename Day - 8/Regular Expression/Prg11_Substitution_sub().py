# WAP using sub() method of regular expression

# sub() this function perform substitution or replacement of pattern.
#re.sub(expression,repl,string)

import re
pattern = re.sub('[a-zA-Z]','*','1131 ABCD Zxye Rani')
print(pattern)


# Output = 
# 1131 **** **** ****
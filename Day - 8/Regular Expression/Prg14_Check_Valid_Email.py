# WAP to check valid email id using regular expression.

import re
email = input("Enter the Email ID : ")
pattern = re.fullmatch(r"\w[a-zA-Z0-9._]*@ybit[.]ac[.]in", email)
if pattern:
    print("Valid Email ID")
else:
    print("Invalid Email ID")


# Output = 
# Enter the Email ID : rani@gmail.com
# Invalid Email ID

# Enter the Email ID : rani@ybit.ac.in
# Valid Email ID
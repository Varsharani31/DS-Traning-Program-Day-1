# WAP to check valid mobile number using regular expression.

import re
no = input("Enter the Mobile Number : ")
obj = re.fullmatch(r"[0-5]\d{9}", no)
if obj:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# Output = 
# Enter the Mobile Number : 9876543210
# Valid Mobile Number

# Output = 
# Enter the Mobile Number : 1928363382
# Valid Mobile Number
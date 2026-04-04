# rstrip() ===> To remove spaces at right hand side
# lstrip() ===> To remove spaces at left hand side
# strip() ===> To remove spaces of both sides

programming = input("Enter your programming name : ")
p_name = programming.strip()
if p_name == 'Python':
    print(p_name)
elif p_name == 'Java':
    print(p_name)
elif p_name == 'Cpp':
    print(p_name)
else:
    print("Wrong programming")


# Output = Enter your programming name : Python
#          Python
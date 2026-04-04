# Positional Argument

def login(username,password):
    if username == password:
        print("Login Successful")
    else:
        print("Invalid Credentials")

username = input("Enter Username : ")
password = input("Enter Password : ")

login(username,password)

# Output = Enter Username : Kiddo
#          Enter Password : Kiddo
#          Login Successful
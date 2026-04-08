# WAP give the count of special characters and whitespaces in the input so it is easy to decode the msg

a = input("Enter a msg : ")
count = 0

for i in a:
    if not i.isalnum():
        count += 1

print("\nNumber of special characters and whitespaces : ",count)
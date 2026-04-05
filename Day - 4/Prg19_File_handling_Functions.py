# WAP for File Handling Functions

f = open("file.txt", "w")
print("Name of File : ", f.name)
print("Mode of File : ", f.mode)
print("Readable : ", f.readable())
print("Writable : ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)

# Output = 
# Name of File :  file.txt
# Mode of File :  w
# Readable :  False
# Writable :  True
# Is File Closed :  False
# Is File Closed :  True
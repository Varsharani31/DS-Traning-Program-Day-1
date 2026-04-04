# WAP to find the key with the minimum value in a dictonary

a = {"X":20,"Y":10,"Z":30}
b=[]

for x in a.values():
    b.append(x)

if b[0]<b[1] and b[0]<b[2]:
    print(b[0], "is minimum")
elif b[1]<b[0] and b[1]<b[2]:
    print(b[1], "is minimum")
else:
    print(b[2]," is minimum")               

# Output = 10 is minimum
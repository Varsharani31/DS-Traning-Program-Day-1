#WAP to take input [2,-1,-3,4,5,-6] and give output of [2,-1.4,-3,5,-6]

a = [2,-1,-3,4,5,-6]

b = []
c= []

for i in a:
    if i > 0 :
       b.append(i)

    else:
        c.append(i)

d = []
for i in range(len(b)):
    d.append(b[i])
    d.append(c[i])
print(d)                                # Output = [2, -1, 4, -3, 5, -6]

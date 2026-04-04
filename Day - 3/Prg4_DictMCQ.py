# Q.1 

a = {(1,2):1,(2,3):2,(4,5):3}
print(a[4,5])                       # Output = 3

# Q.2

a = {'a':1,'b':2,'c':3}
print(a['a','b'])                  # Output = KeyError: ('a', 'b')

# Q.3

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] +=1 
print(arr)                          # Output = {1: 2, '1': 2}

sum = 0
for k in arr:
    sum += arr[k]
print(sum)                          # Output = 4


# Q.4

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)                     # Output = {1: 4, '1': 2}

sum = 0
for k in my_dict:
    sum += my_dict[k]
print(sum)                          # Output = 6


# Q.5

my_dict = {}

my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]
print(sum)                         # Output = 30
print(my_dict)                     # Output = {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}


# Q.6

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(crates)
print(len(crates[box]))           # Output = TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')


# Q.7

dict = {'c':97,'a':96,'b':98}
for _ in sorted(dict):
    print(dict[_])

# Output = # 96
           # 98
           # 97


# Q.8

rec = {"Name":"Python","Age":"20"}
r = rec.copy()
print(id(r)==id(rec))               # Output = False


# Q.10

rec = {"Name":"Python","Age":"20","Addr":"NJ"}
id1 = id(rec)
del rec
rec = {"Name":"Python","Age":"20","Addr":"NJ"}
id2 = id(rec)
print(id1 == id2)                                         # Output = True
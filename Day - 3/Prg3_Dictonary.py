# Dictonary Operations

my_dict = {
    101:"Rani",
    102:"Rani",
    "103":"Saniya",
    "104":"Sneha",
    101:"Varsha",
    104:"Rani"
}

print(my_dict)                      # Output = {101: 'Varsha', 102: 'Rani', '103': 'Saniya', '104': 'Sneha', 104: 'Rani'}

# with the help of key we have to print values

a = my_dict[102]
print(a)                            # Output = Rani


# We will replace old value by new value

my_dict[102] = "Manas"
print(my_dict)                      # Output = {101: 'Varsha', 102: 'Manas', '103': 'Saniya', '104': 'Sneha', 104: 'Rani'}

# Only print key x = 0, 1

for x in my_dict:
    print(x)                        

# Output =  # 101
            # 102
            # 103
            # 104
            # 104


# Only print values

for x in my_dict.values():
    print(x)

# Output =    Varsha
            # Manas
            # Saniya
            # Sneha
            # Rani

# Printing Keys and Values Both

for x,y in my_dict.items():
    print(x,y)

# Output =    101 Varsha
            # 102 Manas
            # 103 Saniya
            # 104 Sneha
            # 104 Rani


# If I have to add new key and value pair in my dictonary

my_dict["Mobile_No"]= 1234567899
print(my_dict)                          

# Output = {101: 'Varsha', 102: 'Manas', '103': 'Saniya', '104': 'Sneha', 104: 'Rani', 'Mobile_No': 1234567899}


# If we want to remove pair by specific key name

my_dict.pop('104')
print(my_dict)              # Output = {101: 'Varsha', 102: 'Rani', '103': 'Saniya', 104: 'Rani'}
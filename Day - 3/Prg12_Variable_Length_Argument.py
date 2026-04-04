# Variable Length Argument / Variable Number of Arguments

def nameOfCitys(*city):                                             # * is used to select all arguments
    print("City Names : ",city)

nameOfCitys("Goa","Nagpur","Mumbai","Pune","Nashik")

# Output = City Names :  ('Goa', 'Nagpur', 'Mumbai', 'Pune', 'Nashik')
# WAP to sort dictionary by Key or Values in ascending or Descending Order.

dict1 = {"C":3,"B":2,"A":1}
print(dict1)

sorted_dict = sorted(dict1.items())
print(sorted_dict)

sorted_dict = sorted(dict1.items(), reverse=True)
print(sorted_dict)

# Output = 
# {'C': 3, 'B': 2, 'A': 1}
# [('A', 1), ('B', 2), ('C', 3)]
# [('C', 3), ('B', 2), ('A', 1)]
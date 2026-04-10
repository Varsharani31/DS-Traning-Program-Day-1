# WAP to calculate the power of a number using recursion.

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

print(power(2, 0))
print(power(2, 2))
print(power(2, 4))

# Output =
# 1
# 4
# 16
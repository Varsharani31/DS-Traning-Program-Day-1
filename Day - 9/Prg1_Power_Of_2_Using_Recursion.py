# WAP to calculate the power of 2 using recursion.

# We use recursion when we know that a problem can be divided into smaller sub problems.

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return 2 * power

print(powerOfTwo(5))

# Output = 32
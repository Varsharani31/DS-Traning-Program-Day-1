# WAP to check if a string is a palindrome using recursion.

def isPalindrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[len(s)-1]:
        return False
    return isPalindrome(s[1:-1])                                # it passes sub strings of main string 

print(isPalindrome("awesome"))
print(isPalindrome("foobar"))
print(isPalindrome("tacocat"))
print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("amanaplanacanalpanamonium"))

# Output =
# False
# False
# True
# True
# False
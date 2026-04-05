# WAP to Count Consonant and Vowels using While Loop
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowels = 0
consonants = 0

string = input("Enter a String : ")

for a in string:
    if a in vowel:
        vowels += 1
    else:
        consonants += 1

print("Number of Vowels : ", vowels)
print("Number of Consonants : ", consonants)


# Output = 
# Enter a String : Varsharani
# Number of Vowels :  4
# Number of Consonants :  6
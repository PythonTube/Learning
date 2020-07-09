vowels = 0
consonants = 0

word = input("Word: ")

for i in word:
    if i.lower() in "aeiou":
        vowels = vowels + 1
    elif i == " ":
        pass
    else:
        consonants = consonants + 1
    
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

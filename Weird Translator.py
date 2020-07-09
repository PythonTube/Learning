original = input("Please enter a sentence: ").strip().lower()

words = original.split() # Split sentence into words

new_words = [] # Create a list

for word in words: # Loop through list and convert
    if word[0] in "aeiou":
        new_word = word + "by"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_end = word[vowel_pos:]
        new_word = the_end + cons + "ay"
        new_words.append(new_word)
        
output = " ".join(new_words)
print(output)

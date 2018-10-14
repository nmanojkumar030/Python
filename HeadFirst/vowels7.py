vowels = {'a', 'e', 'i', 'o', 'u'}
found = {}
word = input("Provide a word to search for vowels: ")

found = vowels.intersection(word)

for letter in found:
    print(letter)


    

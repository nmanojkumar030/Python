vowels = ['a', 'e', 'i', 'o', 'u']
found = {}
word = input("Provide a word to search for vowels: ")
#word = "Milliways"

for letter in word:
    if letter in vowels:
        # This construct avoids key error
        found.setdefault(letter,0)
        found[letter] += 1

for K,V in sorted(found.items()):
    print(K, 'was found', V, 'times')


    

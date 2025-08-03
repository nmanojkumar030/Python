def search4vowels(word:str) -> set:
    """ Display vowels present in the word supplied"""
    vowels = set('aeiou')
    return vowels.intersection(word)


        

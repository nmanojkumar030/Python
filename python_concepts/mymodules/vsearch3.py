def search4vowels(word: str) -> set:
    """Display vowels present in the word supplied"""
    vowels = set("aeiou")
    return vowels.intersection(word)


def search4letters(phrase: str, letters: str = "aeiou") -> set:
    """Display letters present in the phrase supplied"""
    return set(letters).intersection(phrase)

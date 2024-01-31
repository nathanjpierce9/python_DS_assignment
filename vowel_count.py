def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    vowel = set('aeiou')
    vowel_dict = {}
    for char in phrase:
        if char in vowel:
            vowel_dict[char] = vowel_dict.get(char, 0) + 1
    return vowel_dict

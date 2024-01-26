def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    output = ""
    for char in phrase:
        if char == to_swap.upper():
            output += char.lower()
        elif char == to_swap.lower():
            output += char.upper()
        else:
             output += char
    return output
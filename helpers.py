import string


def alphabet_position(character):
    alphabet = string.ascii_lowercase
    lower = character.lower()
    return alphabet.index(lower)


def rotate_character(char, rot):
    alphabet = string.ascii_lowercase

    rotated_idx = (alphabet_position(char) + rot) % 26 
    
    if char.isupper():  
        rotated = alphabet[rotated_idx].upper()
    else:  
        rotated = alphabet[rotated_idx]

    return rotated  
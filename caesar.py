from helpers import alphabet_position, rotate_character

import string
   


def encrypt(text, rot):
    rotated = ''
    alphabet = string.ascii_lowercase

    for char in text:
        if char.lower() in alphabet:
            rotated += rotate_character(char, rot)
        else:
            rotated += char     
    return rotated   


def main():
    print(encrypt(input("Type a message:"), int(input("Rotate by:")))) 

if __name__ == "__main__":
    main()
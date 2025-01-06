from sympy import*
from basics import *

def encrypt(message, key):
    ciphertext = ""
    for letter in message:
        ind = ord(letter) - 97
        new_letter = key[ind]
        ciphertext += new_letter
    print(ciphertext)

def get_key():
    key = ''
    while (not key.isalpha()) or (len(key) != 26) or (len(set(key)) != 26):
        key = input('Substution cipher key: ').lower()
    return key
        
def substitution(inp):
    if inp == "e":
        # work all in lowercase 
        message = get_message().lower()

        key = get_key ()

        # encrypt 
        encrypt(message, key)
        
    elif inp == "d":
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        key = get_key ()

        ciphertext = input("Ciphertext: ")

        alphabet_dict = {"a" : "a"} # initialize dictionary
        key = key.lower()
        i = 0
        for letter in key:
            alphabet_dict[letter] = alphabet[i]
            i += 1

        plaintext = ""

        for letter in ciphertext:
            plaintext += alphabet_dict[letter]

        print(f'Deciphered plaintext: {plaintext}')



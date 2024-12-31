from sympy import*
import random
from basics import *

def substitution(inp):
    if inp == "e":
        # work all in lowercase 
        message = get_message().lower()

        def get_key():
            key = ''
            while (not key.isalpha()) or (len(key) != 26) or (len(set(key)) != 26):
                key = input('Substution cipher key: ').lower()
            return key
        # print something about how the first of the key is a, second is b, and so on
        key = get_key ()

        # encrypt 
        ciphertext = ""
        for letter in message:
            ind = ord(letter) - 97
            new_letter = key[ind]
            ciphertext += new_letter
        print(ciphertext)
    elif inp == "d":
        print("not yet available")


from basics import *
from sympy import*

def caesar(inp):
    if inp == "e":
        message = get_message()

        # find key to shift by
        key = ""
        while not key.isdigit():
            key = input("Shift by: ")
        key = int(key)

        message = message.replace(" ", "").upper()

        # add spaces in message
        new_message = split_5(message)
        key = key % 26

        # encrypt
        ciphered = ""
        for letter in new_message:
            if letter == ' ': 
                ciphered += " "
            elif (ord(letter) + key) <= 90:
                ciphered += chr(ord(letter) + key)
            else:
                ciphered += chr(64 + (ord(letter) + key) % 90)

        print(f'Ciphertext: {ciphered}')
    elif inp == "d":
        ciphertext = get_message()
        ciphertext = split_5(ciphertext)
        max = 0 # keeps track of score of each deciphered text
        # list of common english words
        commons = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you"]
        plaintext = ""
        best_key = 0
        for key in range (1, 26):
            deciphered = ""
            for letter in ciphertext:
                if letter.isupper():
                    if 65+key <= ord(letter) <= 90:
                        deciphered += chr(ord(letter)-key)
                    if 65 <= ord(letter) < 65+key:
                        deciphered += chr((90-64) + (ord(letter)-key))
                else:
                    if 97+key <= ord(letter) <= 122:
                        deciphered += chr(ord(letter)-key)
                    if 97 <= ord(letter) < 97+key:
                        deciphered += chr((122-96) + (ord(letter)-key))
            match_score = 0
            deciphered_lower = deciphered.lower()
            for word in commons:
                found = deciphered_lower.find(word)
                if found != -1:
                    match_score += 1
            if match_score > max:
                max = match_score
                plaintext = deciphered
                best_key = key
        print(f"Deciphered plaintext: {plaintext}")
        print(f'Shifted by: {best_key}')
        print(f'Score: {max}')

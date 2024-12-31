from sympy import*
import random
from basics import *


def affine():
    message = get_message().upper()

    # divide message into 5 letter blocks
    message = split_5(message)

    key1=0
    key2=0
    #while not key1.isdigit():
    key1 = input("Key 1 (slope): ")
    #while not key2.isdigit():
    key2 = input("Key 2 (intercept): ")

    p = prime(random.randint(70000,100000))
    
    # divide message into chunks and encrypt (ciphertext is a list)
    print(f'Your prime is: {p}')
    if len(message)<len(p):
        ciphertext = ""
        for letter in message:
            if letter != " ":
                ciphertext += (str(ord(letter)-64)).zfill(2)
            else:
                continue
        print(f"Encoded message: {ciphered}")
    else:
        ciphertext = []
        for i in range(0, len(message), len(message)/len(p) - 1):
            part_message = message[i, i+(len(message)/len(p) - 1)]
            ciphered=''
            for letter in part_message:
                if letter != " ":
                    ciphered += (str(ord(letter)-64)).zfill(2)
                else:
                    continue
            ciphertext.append(ciphered)

        
    #print(f"Encoded message: {ciphertext}")
    ciphertext = int(ciphertext)

    ciphertext = (key1*ciphertext + key2) % p
    print(f"Ciphertext: {ciphertext}")
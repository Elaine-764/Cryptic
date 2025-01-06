import sympy
import random
from basics import *


def affine(inp):
    if inp == "e":
        message = get_message().upper()

        # divide message into 5 letter blocks
        message = split_5(message)

        print("Key 1 (slope): ")
        key1 = get_num_key()  # Ensure this function returns a value
        print(f"Key 1 (slope) entered: {key1}")

        print("Key 2 (intercept): ")
        key2 = get_num_key()  # Ensure this function returns a value
        print(f"Key 2 (intercept) entered: {key2}")


        p = sympy.prime(random.getrandbits(8))
        #print(p)
        
        # divide message into chunks and encrypt (ciphertext is a list)
        print(f'Your prime is: {p}')
        len_p = len(str(p))
        listof_plain = split(message, len_p - 1)
        print(listof_plain)

        ciphered = []
        for item in listof_plain:
            num = convert_to_ascii(item)
            num = ((key1 * num) + key2) % p
            ciphered.append(num)

        print(f"Ciphertext: {ciphered}")

    elif inp == "d":
        print("Key 1 (slope): ")
        key1=get_num_key() 
        print("Key 1 (intercept): ")
        key2=get_num_key()
        print("Prime (p): ")
        key1=get_num_key()

        listof_ciphertext=input("Input ciphertexts, separated by space if there are multiple: ").split()

        #for ciphered in listof_ciphertext: 


#affine('e')



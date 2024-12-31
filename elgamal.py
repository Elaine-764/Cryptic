import random
from sympy import*
from basics import*
import numpy as np

def elGamal(inp):
    if inp=="k":
        p = prime(random.getrandbits(64))
        g = random.randint(2, p)
        a = random.randint(2, random.getrandbits(64))

        A = pow(g, a, p)
        print(f'Public key (A): {A}')
        print(f'Group (p): {p}')
        print(f'Public key (g): {g}')
        print(f'Private key (a): {a}')

    elif inp=='e':
        print("Public key (g): ")
        g = get_num_key()
        print("Public key (A): ")
        A = get_num_key()
        print(f'Group (p): ')
        p = get_num_key()

        message = get_message().replace(" ", '')

        sp = np.ceil(len(str(p)) / 2)
        listof_messages = split(message, sp)

        k = random.randint(2, p)
        print(f'Private key (k): {k}')
        
        c = pow(g, k, p)
        d = []
        for m in listof_messages:
            num = convert_to_ascii(m)
            d.append(num*pow(A, k, p))
        print('Ciphertexts:')
        print(f'c: {c}')
        print(f'd: {d}')
    
    elif inp=='d':
        print("Private key (a): ")
        a = get_num_key()
        print(f'Group (p): ')
        p = get_num_key()
        print("Ciphertext (c): ")
        c = get_num_key()

        d = input("Ciphertext (d), enter with space in between if there are multiple: ").split()

        e = pow(pow(c, a, p), -1, p)
        plaintext = ""
        for message in d:
            deciphered = (e*d) % p
            plain = convert_from_ascii(deciphered)
            plaintext += plain

        print(f"Deciphered plaintext: {plaintext}")
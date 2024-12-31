from sympy import*
from basics import *

from cryptography.hazmat.primitives.asymmetric import rsa

def my_rsa(inp):
    if inp=="k":
        # generate private keys 
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Extract key components
        private_numbers = private_key.private_numbers()
        public_numbers = private_numbers.public_numbers

        n = public_numbers.n  # Modulus
        e = public_numbers.e  # Public exponent
        d = private_numbers.d  # Private exponent

        p = private_numbers.p  # First prime factor
        q = private_numbers.q  # Second prime factor

        # Print the components
        print("n (modulus):", n)
        print("e (public exponent):", e)
        print("d (private exponent):", d)
        print("p (prime 1):", p)
        print("q (prime 2):", q)

    elif inp=="e":
        print("Public key (N): ")
        #N = get_num_key()
        e = 65537
        print(f"Public exponent (e): {e}")
        
        # convert message into numbers, split by 300 characters, preserving upper/lower case
        message = get_message().replace(" ", '')

        # split message into chunck of 300 characters
        listof_message = split(message, 300)
        listof_ciphertext = []
        for m in listof_message:
            plaintext = int(convert_to_ascii(m))
            ciphered = pow(plaintext, e, N)
            listof_ciphertext.append(ciphered)
        print(f'Ciphertext: {listof_ciphertext}')
    
    elif inp=='d':
        print("Public key (N): ")
        N = get_num_key()
        print("Private exponent (d): ")
        d = get_num_key()

        listof_ciphertext=input("Input ciphertexts, separated by space if there are multiple: ").split()
        plaintext = ""
        for ciphered in listof_ciphertext:
            result = pow(int(ciphered), d, N)
            plain = convert_from_ascii(result)
            plaintext+= plain
        print(f'Deciphered Plaintext: {plaintext}')

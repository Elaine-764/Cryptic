import math
def get_message():
    message = ''
    while not message.isalpha():
        message = input("Message: ").replace(" ", "")
    return message
# removes spaces but preserves upper/lower case

def split_5(message):
    message = message.replace(' ', '')
    new_message = ""
    for j in range(0, len(message), 5):
        partial = message[j:j+5]
        new_message += partial + " "
    return new_message

def split(message, sp):
    out = []
    length = len(message)
    for i in range(math.ceil(length/sp)):
        out.append(message[sp*i:sp*(i+1)])
    return out

# get cipher type
def get_input():
    # find encryption method
    methods = ['c', 'v', 'rsa', 's', 'a']
    encryption = ''
    while not encryption in methods:
        encryption = input("Which encryption method: \n"
                        "[c] Caesar Shift\n"
                        '[v] Vigenere \n'
                        '[rsa] RSA \n'
                        '[a] Affine Cipher\n'
                        '[s] Substitution Cipher \n')
    return  encryption

# encryption/decryption/key setup
def get_input2():
    methods = ['d', 'e', 'k']
    encryption = ''
    while not encryption in methods:
        encryption = input("Encrypt or Decrypt: \n"
                        '[e] encrypt \n'
                        '[d] decrypt \n'
                        '[k] key generation (only for RSA) \n')
    return  encryption

shift = 50
def convert_to_ascii(message):
    new = ""
    for letter in message:
        new += str(ord(letter) - shift)
    return int(new)

def convert_from_ascii(num):
    new = ""
    num = str(num)
    length = len(num)
    for i in range(math.ceil(length/2)):
        new+=chr(shift + int(num[2*i : 2*(i+1)]))
    return new
                       
def get_num_key():
    key = ""
    while not key.isdigit():  
        key = input()
    return int(key)


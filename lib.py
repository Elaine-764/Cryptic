from sympy import*
from basics import *
from caesar import caesar
from substitution import substitution
from affine import affine
from my_rsa import my_rsa
from elgamal import elGamal


def main():
    type = get_input()
    type2 = get_input2()
    if type == "c":
        caesar(type2)
    elif type == "rsa":
        my_rsa(type2)
    elif type == 's':
        substitution()
    elif type == 'a':
        affine()
    elif type == "el":
        elGamal(type2)
    

main()

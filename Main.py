from ciphers.Caesarcipher import cipher_encode
from ciphers.Columnar import columnar_encode
from ciphers.Vatsyayana import encode_Vatsyayana
from ciphers.vigenere import encode_Vigenere
from enigma.enigma_cy import *


from enigma.crackenigma import * 

def userin(choices):
    while True:
        try:
            userin = int(input())
            if userin in choices:
                return userin
        except ValueError:
            pass



def encode():
    print("Text :")

    text = input()


    print("1) Caesar cipher")
    print("2) Columnar transposition cipher")
    print("3) Vatsyayana cipher")
    print("4) Vigenere cipher")
    print("5) Enigma")
    cipher = userin([1,2,3,4,5])

    if cipher == 1:
        print("Key (0-26)")
        key = int(input())
        print(cipher_encode(text,key))

    elif cipher == 2:
        print("Key (\"1,7,3,5\")")
        key = input()
        key = key.split(",")

        print(columnar_encode(text,key))

    elif cipher == 3:
        print("Key (\"ab,cd,ef,gh,ij\") (paren niet dubbel en alles moet een paar vormen)")
        key = input()
        print(encode_Vatsyayana(text,key))

    elif cipher == 4:
        print("Key (\"wachtwoord\") (kan gewoon een woord zijn)")
        key = input()
        print(encode_Vigenere(text,key))

    elif cipher == 5:
        print("Rotor Order (\"I,II,III\") (<-- keuze uit deze 3")
        order = input().split(",")
        rotororder = [rotors[len(i)-1] for i in order]
        turnoverorder = [turnovers[len(i)-1] for i in order]

        print("Offsets (\"17,1,26\") (0-26)")
        offsets = [int(i) for i in input().split(",")]
        print("plugboard (\"abcded\") (combinaties dus a en b wordt ab, kan leeg gelaten worden)")
        plugboard = create_plugboard(input())

        print(encode_enigma(plugboard, rotororder, offsets,turnoverorder, reflw, text))


#1 encode
#2 decode
#3 crack

print("1) encode")
print("2) decode")
print("3) crack")


menu = userin([1,2,3])

if menu == 1:
    encode()

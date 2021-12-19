import sys
COUNTED = "abcdefghijklmnopqrstuvwxyz"

tekst = "YGEFNQNADQPFARUSGDQFTUEAGF" # wat je wil versleutelen
sleutel = -64 # geheime sleutel

# ZELFINPUT aan als je zelf wilt invoeren tijdens running van het programmad
ZELFINPUT = False
if ZELFINPUT:
    tekst = input("Tekst: ")
    sleutel = int(input("Sleutel: "))


if len(sys.argv)>1:
    sleutel = int(sys.argv[1])
    with open(sys.argv[2], "r", encoding="utf8") as file:
        tekst = file.read()

# tekst allemaal kleine letters van maken en spaties weg halen
tekst = tekst.lower()
tekst = ''.join([i for i in tekst if i in COUNTED])
# ceasar cipher
resultaat = "".join(chr((ord(i) + sleutel - 97) % 26 + 97) for i in tekst) # verplaats letter met key hoeveelheid naar voren

if len(sys.argv)>3:
    
    with open(sys.argv[3], 'w',encoding="utf-8") as f:
        f.write(resultaat)
    print("done")
else:
    print(f"originele tekst    : {tekst}")
    print(f"sleutel            : {sleutel}")
    print(f"versleutelde tekst : {resultaat}")



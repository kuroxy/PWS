tekst = "De sleutel opent het slot van de kist" # wat je wil versleutelen
sleutel = 0 # geheime sleutel

# ZELFINPUT aan als je zelf wilt invoeren tijdens running van het programmad
ZELFINPUT = False
if ZELFINPUT:
    tekst = input("Tekst: ")
    sleutel = input("Sleutel: ")

# tekst allemaal kleine letters van maken en spaties weg halen
tekst = tekst.lower()
tekst = tekst.replace(" ","")

# ceasar cipher
resultaat = "".join(chr((ord(i) + sleutel - 97) % 26 + 97) for i in tekst) # verplaats letter met key hoeveelheid naar voren
print(f"originele tekst    : {tekst}")
print(f"sleutel            : {sleutel}")
print(f"versleutelde tekst : {resultaat}")



from math import ceil
import sys
COUNTED = "abcdefghijklmnopqrstuvwxyz"

text = """Uiteindelijk is gekozen om het concept met de takelaandrijving te fabriceren. 
Als touw gebruiken we een nylon draad van één millimeter dik, deze is namelijk heel sterk en verminderd de kans op knopen.
De draad loopt vanuit een spoel omhoog en is iets voor het contragewicht bevestigd aan de brug. 
De draad zit vast met een knoop tussen een moer en de kop van een bout. 
De motor bevindt zich onder het wegdek en is verbonden met een 8mm stalen staaf doormiddel van motorkoppelstukken. 
Aan beide weerzijden van de motor zijn kogellagers aangebracht in het hout waar de stalen staaf doorheen loopt. 
Aan het uiteinde van de stalen staven bevinden zich zelfgemaakte spoelen. 
De motor wordt aangedreven door een H-brug waar een spanning van 9v op staat
We gebruiken servos voor de slagbomen, deze zijn naast het wegdek gemonteerd. 
Het montuur en de slagboom zelf is met een 3D-printer gemaakt. 
We gebruiken ook LED lichten voor de stoplichten, beide kanten van het wegdek zijn voorzien van een rode, gele en groene LED lichten. Ook beide kanten van het kanaal zijn voorzien van rode en groene lichten. 
Om te detecteren dat vaarverkeer door het kanaal wil varen hebben we IR-sensoren gebruikt. We hebben voor IR-sensoren gekozen omdat deze gemakkelijker zijn in gebruik en programmering. 
Om de windkracht te meten gebruiken we een ventilator, wanneer deze draait ontstaat er een spanning die ingelezen kan worden. 
De ventilator is hoog gemonteerd in dezelfde richting als het wegverkeer, dit is gedaan omdat wind vanuit deze richting het gevaarlijkst is voor de brug. 
De noodstop is geregeld door schakelaar, wanneer deze wordt geactiveerd maakt de brug de huidige sequentie af en blijft de brug gesloten tot de schakelaar wordt gedeactiveerd. 
Alle functies van de brug worden aangestuurd met een Arduino."""
key = "ah,bk,co,dv,ex,ft,gq,iu,jm,lz,nw,py,rs"
#4,3,5,1,2,0

key = key.lower()
key = key.split(",")

crypt = {}
for comb in key:
    crypt[comb[0]] = comb[1]
    crypt[comb[1]] = comb[0]

print(crypt)
text = text.lower()
text = ''.join([i for i in text if i in COUNTED])

result = "".join(crypt[char] for char in text)

print(result)




key = "ah,bk,co,dv,ex,ft,gq,iu,jm,lz,nw,py,rs"
#4,3,5,1,2,0

def key_from_list(keylist):
    key = keylist.lower()
    key = key.split(",")

    crypt = {}
    for comb in key:
        crypt[comb[0]] = comb[1]
        crypt[comb[1]] = comb[0]
    return crypt


def vatsyayana_encode(key,text):
    text = text.lower()
    text = ''.join([i for i in text if i in COUNTED])

    return "".join(crypt[char] for char in text)

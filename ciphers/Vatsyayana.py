

def val_to_char(val: int):
    return chr(val+65).lower()


def char_to_val(c: str):
    return ord(c.upper())-65


def encode_Vatsyayana(text:str,key:str):
    key = key.lower()
    key = key.split(",")
    encoder = list(range(26))
    for i in key:
        p = char_to_val(i[0])
        q = char_to_val(i[1])
        encoder[p] = q
        encoder[q] = p
    text = text.lower()
    text = ''.join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz"])

    return "".join(val_to_char(encoder[char_to_val(char)]) for char in text)


if __name__ == '__main__':
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


    result = encode_Vatsyayana(text,key)

    print(result)


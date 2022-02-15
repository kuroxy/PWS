import sys

def cipher_encode(text, key):
    # tekst allemaal kleine letters van maken en spaties weg halen
    text = text.lower()
    text = ''.join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz"])
    return "".join(chr((ord(i) + key - 97) % 26 + 97) for i in text) # verplaats letter met key hoeveelheid naar voren




if __name__ == '__main__':

    tekst = "YGEFNQNADQPFARUSGDQFTUEAGF" # wat je wil versleutelen
    sleutel = -64 # geheime sleutel
    
    ZELFINPUT = False
    # ZELFINPUT aan als je zelf wilt invoeren tijdens running van het programmad
    
    if ZELFINPUT:
        tekst = input("Tekst: ")
        sleutel = int(input("Sleutel: "))


    if len(sys.argv)>1:
        sleutel = int(sys.argv[1])
        with open(sys.argv[2], "r", encoding="utf8") as file:
            tekst = file.read()


    # ceasar cipher
    resultaat = cipher_encode(tekst,sleutel) # verplaats letter met key hoeveelheid naar voren

    if len(sys.argv)>3:
        
        with open(sys.argv[3], 'w',encoding="utf-8") as f:
            f.write(resultaat)
        print("done")
    else:
        print(f"originele tekst    : {tekst}")
        print(f"sleutel            : {sleutel}")
        print(f"versleutelde tekst : {resultaat}")



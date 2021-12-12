from math import ceil
# sourcery skip: use-join
tekst = "De sleutel opent het slot van de kist" # wat je wil versleutelen
sleutel = "desleutel" # geheime sleutel


# tekst allemaal kleine letters van maken en spaties weg halen
sleutel = sleutel.lower()
sleutel = sleutel.replace(" ","")
sleutellist = list(sleutel)

tekst = tekst.lower()
tekst = tekst.replace(" ","")

sleutellengte = len(sleutel)


# ColumnarTransposition
rijen = [[sleutel[i]] for i in range(sleutellengte)]

for letterindex in range(len(tekst)):
    rijen[letterindex%sleutellengte].append(tekst[letterindex])

cipherrij = sorted(rijen)

versleuteldetekst = ""
for i in cipherrij:
    for letter in range(1,len(i)):
        versleuteldetekst+= i[letter]

print(f"originele tekst    : {tekst}")
print(f"sleutel            : {sleutel}")
print()
print(" ".join(i[1] for i in rijen))
print("-"*len(rijen)*2)
for i in range(len(tekst)):
    if i%sleutellengte ==0 and i!=0:
        print()
    print(f"{tekst[i]} ",end="")
print("\n")

print(" ".join(i[1] for i in cipherrij))
print("-"*len(rijen)*2)
for i in range(ceil(len(tekst)/sleutellengte)):
    for j in range(len(cipherrij)):
        if i < len(cipherrij[j])-1:
            print(f"{cipherrij[j][i+1]} ",end="")
    print()
print()
print(f"versleutelde tekst : {versleuteldetekst}")

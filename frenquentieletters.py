import matplotlib.pyplot as plt
import sys
from collections import Counter


COUNTED = "abcdefghijklmnopqrstuvwxyz"

maxgraphamount = 26**2
graphsorted = True
graphalphasorted = False
graphnormalized = True

counter = []
amount = 2
previous = []

file = "texts/nederlandseboeken/insitituutsparrenheide.txt"
tekst = """
John Brooke deed een jaar lang manmoedig zijn plicht en werd gewond
naar huis gezonden; en toen hij eenmaal daar was, liet men hem niet
weer vertrekken. Hij ontving geen eerekruisen of ridderorden, hoezeer
hij ze ook verdiende, daar hij blijmoedig al wat hij bezat op het spel
had gezet; want het volle leven en een jeugdige liefde zijn kostbare
zaken. Volkomen verzoend met zijn ontslag, deed hij al het mogelijke
om zijn gezondheid terug te krijgen, opdat hij aan het werk kon gaan
om voor Meta een eigen huis te verdienen. Zijn gezond verstand en fier
gevoel van onafhankelijkheid deden hem de edelmoedige aanbiedingen van
den heer Laurence afslaan, en een betrekking van tweeden boekhouder
aannemen, daar hij liever wilde beginnen met een eerlijk verdiend
salaris, dan met een moeilijk af te lossen schuld."""


if len(sys.argv) >1:
    file = sys.argv[1]

if file and not tekst:
    with open(file, "r", encoding="utf8") as file:
        tekst = file.read()


tekst = tekst.lower()
tekst = ''.join([i for i in tekst if i in COUNTED])

for char in tekst:
    previous.append(char)

    if len(previous) > amount:
        previous.pop(0)

    if len(previous) == amount:
        counter.append("".join(previous))

print("Done analyzing")
total = len(counter)

counter = dict(Counter(counter))
print("Done Counting")

if graphsorted:
    counter = dict(sorted(counter.items(), key=lambda item: -item[1]))

if graphalphasorted:
    counter = dict(sorted(counter.items()))

if graphnormalized:
    
    for comb in counter:
        counter[comb]/=total

print(counter)
letters = [*counter]# a,b,c,d,e,,,
kansen = list(counter.values())

plt.bar(letters[0:min(maxgraphamount,len(letters))],kansen[0:min(maxgraphamount,len(kansen))]) 
plt.title('Frequentie van letters')
plt.xlabel('Letter')
plt.ylabel('Kans')

if len(sys.argv) > 2:
    plt.savefig(sys.argv[2])
else:
    plt.show()
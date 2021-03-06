import matplotlib.pyplot as plt
import sys
from collections import Counter


COUNTED = "abcdefghijklmnopqrstuvwxyz"

maxgraphamount = 26**2
graphsorted = False
graphalphasorted = True
graphnormalized = True

counter = []
amount = 1
previous = []

file = "" # texts/nederlandseboeken/insitituutsparrenheide.txt
tekst = """kpapz llucv vyill skchu jhlzh yjpwo ly"""


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
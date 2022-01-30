import sys
from collections import Counter
import pickle

xyaxis = list("abcdefghijklmnopqrstuvwxyz")
COUNTED = "abcdefghijklmnopqrstuvwxyz"



savebigramarray = True
errorbigramfile= "bigram_insitituutsparrenheide.txt.npy"
grapherror = False 

counter = []
previous = []

file = "texts/artikelen.txt"
tekst = """"""


if file and not tekst:
    with open(file, "r", encoding="utf8") as file:
        tekst = file.read()

tekst = tekst.lower()
tekst = ''.join([i for i in tekst if i in COUNTED])

for char in tekst:
    previous.append(char)

    if len(previous) > 4:
        previous.pop(0)

    if len(previous) == 4:
        counter.append("".join(previous))

print("Done analyzing")
total = len(counter)

counter = dict(Counter(counter))
counter = dict(sorted(counter.items(), key=lambda item: -item[1]))

print("Done Counting")

for comb in counter:
    counter[comb]/=total

print(counter)
print(total)

write_file = open("default_quadgram.pkl", "wb")

pickle.dump(counter, write_file)

write_file.close()
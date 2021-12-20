import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
from collections import Counter

xyaxis = list("abcdefghijklmnopqrstuvwxyz")
COUNTED = "abcdefghijklmnopqrstuvwxyz"



savebigramarray = True
errorbigramfile= "bigram_insitituutsparrenheide.txt.npy"
grapherror = False 

counter = []
previous = []

file = "texts/artikelen.txt"
tekst = """"""


if len(sys.argv) >1:
    file = sys.argv[1]

if file and not tekst:
    with open(file, "r", encoding="utf8") as f:
        tekst = f.read()

if errorbigramfile:
    errorbigram = np.load(errorbigramfile)

tekst = tekst.lower()
tekst = ''.join([i for i in tekst if i in COUNTED])

for char in tekst:
    previous.append(char)

    if len(previous) > 2:
        previous.pop(0)

    if len(previous) == 2:
        counter.append("".join(previous))

print("Done analyzing")
total = len(counter)

counter = dict(Counter(counter))
print("Done Counting")

for comb in counter:
    counter[comb]/=total


heatmap = []
for y in xyaxis:
    line = []
    for x in xyaxis:
        xy = f"{y}{x}"
        if xy in counter:
            line.append(counter[xy])
        else:
            line.append(0)
    heatmap.append(line)
heatmap = np.array(heatmap)

if savebigramarray:
    np.save(f"bigram_{file.split('/')[-1]}", heatmap)


if grapherror and errorbigramfile:
    heatmap= (heatmap-errorbigram)
    heatmap = heatmap*heatmap

print(heatmap)
fig, ax = plt.subplots()
im = ax.imshow(heatmap,cmap=plt.cm.plasma)


# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(xyaxis)))
ax.set_xticklabels(xyaxis)
ax.set_yticks(np.arange(len(xyaxis)))
ax.set_yticklabels(xyaxis)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=0, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
"""
for i in range(len(xyaxis)):
    for j in range(len(xyaxis)):
        text = ax.text(j, i, round(heatmap[i, j]*(24**2),2),
                       ha="center", va="center", color="w")
"""
ax.set_title("bigram frequency")

fig.tight_layout()

fig.colorbar(im,ax=ax)
plt.show()

if not grapherror and errorbigramfile:
    heatmap= (heatmap-errorbigram)
    heatmap = heatmap*heatmap


if errorbigramfile:
    totalerrorsq = sum(sum(heatmap))

    print("error : " + str(totalerrorsq))
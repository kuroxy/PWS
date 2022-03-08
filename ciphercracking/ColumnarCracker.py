import numpy as np
from collections import Counter
import math 
import random
import pickle


def countquadgrams(text):  # sourcery skip: use-dict-items
    text = text.lower()
    text = ''.join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz"])
    previous = []
    counter = []

    for char in text:
        previous.append(char)

        if len(previous) > 4:
            previous.pop(0)

        if len(previous) == 4:
            counter.append("".join(previous))

    total = len(counter)
    counter = dict(Counter(counter))

    for comb in counter:
        counter[comb]/=total
    return counter


def calculate_error(quadgram,defaultquadgram):
    totalerr = 0
    for quad in quadgram:
        defval = defaultquadgram[quad] if quad in defaultquadgram else 0
        totalerr+= abs(defval-quadgram[quad])
    return totalerr


def calculate_error_text(text,defaultquadgram):
    quadgram = countquadgrams(text)

    return calculate_error(quadgram,defaultquadgram)


def columnar_decoder(text:str,key:list)->str:

    amount = {i:len(text)//len(key) for i in key}
    for i in range(len(text)%len(key)):
        amount[key[i]]+=1

    rows = {i:[] for i in key}

    total = 0
    for i in sorted(rows):
        for _ in range(amount[i]):
            rows[i].append(text[total])
            total += 1


    result = ""
    for i in range(math.ceil(len(text)/len(key))):
        for row, value in rows.items():
            if len(rows[row])>i:
                result += value[i]
    return result

  
# hill climbing

def fitness_key(key:list,encryptedtext:str,defaultquadgram):
    decoded = columnar_decoder(encryptedtext,key)
    return calculate_error_text(decoded,defaultquadgram)


def getNeighbours(key):                                             # sourcery skip: merge-list-appends-into-extend
    neighbours = []
    for i in range(len(key)):
        for j in range(i + 1, len(key)):
            neighbour = key.copy()
            neighbour[i] = key[j]
            neighbour[j] = key[i]
            neighbours.append(neighbour)
    neighbours.append([key[-1]] + key[:-1])
    neighbours.append(key[1:] + [key[0]])
    return neighbours


def getBestNeighbour(keys,encryptedtext,defaultquadgram):
    bestfitness = math.inf
    bestkey = None
    for key in keys:
        currfitness = fitness_key(key,encryptedtext,defaultquadgram)
        if currfitness < bestfitness:
            bestfitness = currfitness
            bestkey = key
            
    return bestkey,bestfitness
 

def hillclim(startkey,encryptedtext,defaultquadgram):
    currsolution = startkey
    currfitness = fitness_key(currsolution,encryptedtext,defaultquadgram)
    neighbours = getNeighbours(currsolution)
    
    bestneighbour,bestneighbourfitness = getBestNeighbour(neighbours,encryptedtext,defaultquadgram)


    while bestneighbourfitness < currfitness:
        currsolution = bestneighbour
        currfitness = bestneighbourfitness
        neighbours = getNeighbours(currsolution)
        bestneighbour,bestneighbourfitness = getBestNeighbour(neighbours,encryptedtext,defaultquadgram)
    return currsolution,currfitness


# sourcery skip: for-append-to-extend
with open("default_quadgram.pkl", "rb") as quadfile:
    defaultquadgramarray = pickle.load(quadfile)

encryptedtext = "vecasiheloadwpmibamaiieeikoetrsennntpzlgrmtoaiodltonrsstetridolorpoeiamkaebtrvurscdwtenhkg"
encryptedtext = encryptedtext.lower()
keylenrange = [2,15]


bestcases = {}

for keylen in range(*keylenrange):
    key = list(range(keylen))
    bestcases[f"{keylen}"]=[]
    for _ in range(max(2,min(200,2*math.factorial(keylen)))):
        rkey = key.copy()
        random.shuffle(rkey)

        decryptedtext = columnar_decoder(encryptedtext,rkey)
        err = calculate_error_text(decryptedtext,defaultquadgramarray)
        if [err,rkey] not in bestcases[f"{keylen}"]:
            bestcases[f"{keylen}"].append([err,rkey])


bestkeys = []
for keylen in bestcases:
    bestkeylist = sorted(bestcases[keylen])

    for i in range(min(2,len(bestkeylist))):

        bestkeys.append(bestkeylist[i])

bestkeys = sorted(bestkeys)

for key in bestkeys:
    decoded = columnar_decoder(encryptedtext,key[1])
    print(f"{round(key[0],5)} {key[1]} {decoded[:min(len(decoded),50)]}")


keylenuserin = input("Keylength? ")


print("--------")


latestkey = bestcases[keylenuserin][0][1]

while True:
    key,fitness = hillclim(latestkey,encryptedtext,defaultquadgramarray)
    decoded = columnar_decoder(encryptedtext,key)
    print(f"{round(fitness,5)} {key} {decoded[:min(len(decoded),10000)]}")

    userin = input("try again (Q = quit)")
    if userin.lower() == "q":
        break
    latestkey = list(range(int(keylenuserin)))
    random.shuffle(latestkey)


"""
newsols = []
for _ in range(max(2,min(400,2*math.factorial(int(keylenuserin))))):
    rkey = bestkey.copy()
    random.shuffle(rkey)

    decryptedtext = columnar_decoder(encryptedtext,rkey)
    err = calculate_error_text(decryptedtext,defaultquadgramarray)
    if [err,rkey] not in newsols:
        newsols.append([err,rkey])

newsols = sorted(newsols)
for ind,i in enumerate(newsols):
    decoded = columnar_decoder(encryptedtext,i[1])
    print(f"{i} {decoded}")
    if ind > 100:
        break

print(calculate_error_text(columnar_decoder(encryptedtext,[4, 0, 5, 1, 6, 3, 2]),defaultquadgramarray))"""
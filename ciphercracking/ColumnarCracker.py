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
        defval = defaultquadgram[quad] if quad in defaultquadgram else -.1
        totalerr+= (quadgram[quad]-defval)
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




with open("default_quadgram.pkl", "rb") as quadfile:
    defaultquadgramarray = pickle.load(quadfile)

encryptedtext = "ERHBEKOEONDASELEMNHOWJACBGEZGOENUELVE"
encryptedtext.lower()
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
newsols = []

bestkey = bestcases[keylenuserin][0][1]
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
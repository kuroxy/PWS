import numpy as np
from collections import Counter
import math 
import random
import pickle


def vatsyayana_decode(text:str,key:list):
    goodtext = text.lower()
    goodtext = ''.join([i for i in goodtext if i in "abcdefghijklmnopqrstuvwxyz"])

    return "".join(val_to_char(key[char_to_val(char)]) for char in goodtext)


def val_to_char(val):
    return chr(val+65)


def char_to_val(c):
    return ord(c.upper())-65


def create_key(keys): # "ab,cd" a<>b c<>d
    returnlist = list(range(26))
    returnlist.reverse()
    for i in range(0,len(keys),2):
        a = char_to_val(keys[i])
        b = char_to_val(keys[i+1])
        returnlist[a] = b
        returnlist[b] = a
    return returnlist


def countquadgrams(text):
    text = text.lower()
    text = ''.join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz"])
    grams = []

    for i in range(len(text)-3):
        grams.append(text[i:(i+4)])

    total = len(grams)
    counter = dict(Counter(grams))
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


def fitness_key(encryptedtext,key,defaultquadgram):
    decoded = vatsyayana_decode(encryptedtext,key)
    return calculate_error_text(decoded,defaultquadgram)


def getNeighbours(key):
    fulllist = []
    for i in range(26):
        inew = key.copy()
        if inew[i]!=i:
            inew[inew[i]] = inew[i]
            inew[i] = i
        
        for j in range(26):
            new = inew.copy()
            if new[j]!=j:
                new[new[j]] = new[j]
                new[j] = j
            
            new[i] = j
            new[j] = i
            if new not in fulllist:
                fulllist.append(new)
    return fulllist


def getBestNeighbour(encryptedtext,key,defaultquadgram):
    bestfitness = math.inf
    bestkey = None
    for newkey in getNeighbours(key):
        currfitness = fitness_key(encryptedtext,newkey,defaultquadgram)
        if currfitness < bestfitness:
            bestfitness = currfitness
            bestkey = newkey
            
    return bestkey,bestfitness


def hillclim(encryptedtext,key,defaultquadgram):
    currsolution = key
    currfitness = fitness_key(encryptedtext,key,defaultquadgram)
    bestneighbour,bestneighbourfitness = getBestNeighbour(encryptedtext,currsolution,defaultquadgram)


    while bestneighbourfitness < currfitness:
        currsolution = bestneighbour
        currfitness = bestneighbourfitness
        bestneighbour,bestneighbourfitness = getBestNeighbour(encryptedtext,currsolution,defaultquadgram)
    return currsolution,currfitness


with open("default_quadgram.pkl", "rb") as quadgramfile:
    defaultquadgramarray = pickle.load(quadgramfile)
    
encryptedtext = "AHUTSWPGIPGBPQYLBPGVPQDPUHQRVFPUUPQBPQSPGIHJAFBWPZIHXPQWQHLFYVPQGWCFLWRPQWQBPROXQHVFWPZKHHUXHHZFPCLTTGYLIIWPUPGKWJAXPFBPXPWVCPVRPGPPBFYFAPFYESYPGPQBPGVEPPUUWPBCPVIHFKYQRPQBWPUWPTHHQRPZUPPBPXPWVCPVZPLGWRPQIHFXHHZFPQKWCALQBHQVEHVVPQBHHGDWCVFWEFWQBPXHHFKPIPGBPQBHQYYZAHGFPUWCZFYPRPCLWJAFPQKYYSYURBPAPFPPQPQLXXPGSHQAPFEGYRGHXXHYEAPFHQBPGPPGVJAPPQRPPQPWQBPHHQBPQTPPVFBHRFPZYXPQXHHGAPFXYYWVFIPGBAPFFYJAFPRPQBPQHSYQBBHQZKWCAPFKHJAFPKYPUPIPPGZYQBPSPGUWJAFWQRKUHRWYGQYLWFVFPZPQBBYYGRHHQHUUPUHXEWYQVIPGBPQYQFVFYZPQPQKPVJAWFFPGBPQHUVSLGWRPDHUUYQVWQAPFBYQZPGDUHLIPHSYQBBLWVFPGAPFIHVPPQTHQFHVFWVJAFHTPGPPU"
encryptedtext = encryptedtext.lower()


key,fit = hillclim(encryptedtext, create_key(""),defaultquadgramarray)
print(key,fit)
print(vatsyayana_decode(encryptedtext,key))

"""while True:

    latestkey = generate_key()
    key,fitness = hillclim(latestkey,encryptedtext,defaultquadgramarray)
    decoded = vatsyayana_decode(encryptedtext,key)
    print(f"{round(fitness,5)} {key} {decoded[:min(len(decoded),1000)]}")

    userin = input("try again (Q = quit)")
    if userin.lower() == "q":
        break
    

"""


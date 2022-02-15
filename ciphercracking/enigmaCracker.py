import sys
sys.path.append(r'.//ciphers')
import itertools
import math
import enigma 
import random
import pickle
from collections import Counter
import time

with open("default_bigram.pkl", "rb") as bifile:
    defaultbigramarray = pickle.load(bifile)






def IoC(text):
    counter = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    total = 0
    if type(text) != str:
        print(text)
        print(type(text))
    for c in text:
        c = c.lower()
        if c in counter:
            counter[c]+=1
            total+=1

    ic = 0
    for letter in counter:
        ic+= (counter[letter]/total*(counter[letter]-1)/(total-1))
    return ic


def generate_plugboard(plugamount):
    options = "abcdefghijklmnopqrstuvwxyz"
    plugboard = {}
    for _ in range(plugamount):
        first = options[random.randint(0, len(options))]
        options = options.replace(first,"")
        
        second = options[random.randint(0, len(options))]
        options = options.replace(second,"") 


        first = enigma.char_to_val(first)
        second = enigma.char_to_val(second)

        plugboard[first] = second
        plugboard[second] = first
    return plugboard


def random_rotors(duplicates=False):
    rotorchoices = [enigma.rotorI,enigma.rotorII,enigma.rotorIII,enigma.rotorIV,enigma.rotorV]
    rotorlist = []
    for _ in range(3):
        rotor = random.choice(rotorchoices)
        if duplicates==False:
            rotorchoices.remove(rotor)
        rotorlist.append(rotor)
    return rotorlist


def rotor_offset_neighbours(offsetlist):
    neighbours = []
    offset1 = offsetlist[0]
    offset2 = offsetlist[1]
    offset3 = offsetlist[2]
    for i in range(26):
        neighbours.append([i,offset2,offset3])
        neighbours.append([offset1,i,offset3])
        neighbours.append([offset1,offset2,i])

    neighbours.append([offset2,offset3,offset1])
    neighbours.append([offset3,offset1,offset2])
    neighbours.append([offset1,offset3,offset2])
    neighbours.append([offset2,offset1,offset3])

    neighbours.sort()
    neighbours = [k for k,_ in itertools.groupby(neighbours)]

    if offsetlist in neighbours:
        neighbours.remove(offsetlist)
    return neighbours


def countbigrams(text):  # sourcery skip: use-dict-items
    text = text.lower()
    text = ''.join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz"])
    previous = []
    counter = []

    for char in text:
        previous.append(char)

        if len(previous) > 2:
            previous.pop(0)

        if len(previous) == 2:
            counter.append("".join(previous))

    total = len(counter)
    counter = dict(Counter(counter))

    for comb in counter:
        counter[comb]/=total
    return counter


def calculate_error(bigram):
    global defaultquadgramarray
    totalerr = 0
    for bi in bigram:
        defval = defaultbigramarray[bi] if bi in defaultbigramarray else 0
        totalerr+= abs(defval-bigram[bi])
    return totalerr


def calculate_error_text(text):
    quadgram = countbigrams(text)
    return calculate_error(quadgram)


def fitness_key(plugboard,rotorlist,rotoroffset,reflector,encryptedtext:str):
    rotorlist[0].set_offset(rotoroffset[0])
    rotorlist[1].set_offset(rotoroffset[1])
    rotorlist[2].set_offset(rotoroffset[2])
    decoded = enigma.encode_enigma(plugboard,rotorlist,reflector,encryptedtext)
    return calculate_error_text(decoded)

    #return (IoC(decoded)-0.07842040866666836)**2



def getBestNeighbour(plugboard,rotorlist,rotoroffsets,reflector,encryptedtext:str):
    bestfitness = math.inf
    bestkey = None
    for key in rotoroffsets:
        currfitness = fitness_key(plugboard,rotorlist,key,reflector,encryptedtext)
        if currfitness < bestfitness:
            bestfitness = currfitness
            bestkey = key
            
    return bestkey,bestfitness
 


def hillclim(plugboard,rotorlist,rotoroffset,reflector,encryptedtext:str):
    currsolution = rotoroffset
    currfitness = fitness_key(plugboard,rotorlist,rotoroffset,reflector,encryptedtext)
    neighbours = rotor_offset_neighbours(currsolution)
    
    bestneighbour,bestneighbourfitness = getBestNeighbour(plugboard,rotorlist,neighbours,reflector,encryptedtext)
    print(currsolution,currfitness)

    while bestneighbourfitness < currfitness:
        currsolution = bestneighbour
        currfitness = bestneighbourfitness
        neighbours = rotor_offset_neighbours(currsolution)
        bestneighbour,bestneighbourfitness = getBestNeighbour(plugboard,rotorlist,neighbours,reflector,encryptedtext)
        print(currsolution,currfitness)
    return currsolution,currfitness


def crack_offset(plugboard,rotorlist,reflector,encryptedtext):
    bestrotor = {}

    for i in range(26):
        for j in range(26):
            for k in range(26):
                rotorlist[0].set_offset(i)
                rotorlist[1].set_offset(j)
                rotorlist[2].set_offset(k)
                bestrotor[f"{i}|{j}|{k}"] = enigma.encode_enigma(plugboard,rotorlist,reflector,encryptedtext)
                
    bestrotor = dict(sorted(bestrotor.items(), key=lambda item: -IoC(item[1])))

    """
    for i,key in enumerate(bestrotor):
        print(f"{key} : {IoC(bestrotor[key])} : {bestrotor[key][:50]}")
        if i > 100: break"""


text = "PIJRJXTKETNKLHPAGAWJOXQYVJOBEGZTFBVQHTLWGIHKVPPDTVKZFSSPHBGYTHNCODBDWEJRLGPCKNZEUZMQPQMVTFKTKSUUIEEZAEJJMXPVZPNJKUMWVXXFZHBGURHYVFDVFXTUWVXJQBHRSOVGDLZCXFWUUNVAHFMONBVSMIIXEFHNBPGVCHUHPIZSGPRPGVNOOVOZBOIYBBLOITURLECDLLKQWPKXEGKDBROHMNURBHCGWPWHYIAFYKEOUYYEWQJLQGEHKQLCJSLHAMZPAXOTUHMCFJSVHZWMLRGJHROSQFIQYEMDPEHQJXAGLIGEZFEDHFIGITCGJBMOZUPZNZWUDBLTAUGODPOIBJCJZEWNNXKBZTBHVGIGOIMBZHDEIUPDVLUGEBJXGZOPASGJGWUATLPJVMZUGVPBFAFPUCDWDKYITTYIINMGCMAGLNZYTFWUYFPXZKZQRFECFMIHLHPORDUHIAVOZDYMVSFJXNJUNEUSOIQLHAQBDAWOJYZWFLSURGSKQXKCPIDXHOUVVZFKWODKITDQPQWTXTIGRTYHBRHCAFZXACCJTCBIBYBMHRRARKSERVGOKNK"


plugboard = {}
rotorlist = [enigma.rotorI,enigma.rotorII,enigma.rotorIII]


crack_offset(plugboard,rotorlist,enigma.reflectorB,text)

"""

plugboard = {} #generate_plugboard(5)
rotorchoices = [enigma.rotorI,enigma.rotorII,enigma.rotorIII,enigma.rotorIV,enigma.rotorV]
bestrotor = {}
for i in range(10):
    randomoffset= [random.randrange(0,26),random.randrange(0,26),random.randrange(0,26)]
    #randomoffset= [16,17,24]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                if i != j and j != k and i != k:
                    rotorlist = [rotorchoices[i],rotorchoices[j],rotorchoices[k]]
                    rotorlist[0].set_offset(randomoffset[0])
                    rotorlist[1].set_offset(randomoffset[1])
                    rotorlist[2].set_offset(randomoffset[2])

                    if f"{i}{j}{k}" in bestrotor:
                        bestrotor[f"{i}{j}{k}"] += calculate_error_text(enigma.encode_enigma(plugboard,rotorlist,enigma.reflectorB,text))
                    else:
                        bestrotor[f"{i}{j}{k}"] = calculate_error_text(enigma.encode_enigma(plugboard,rotorlist,enigma.reflectorB,text))

bestrotor = dict(sorted(bestrotor.items(), key=lambda item: item[1]))

for key in bestrotor:
    print(f"{key} : {bestrotor[key]}")

print(randomoffset)"""
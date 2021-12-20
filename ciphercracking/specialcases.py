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


def getNeighbours(key):
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


with open("default_quadgram.pkl", "rb") as quadfile:
    defaultquadgramarray = pickle.load(quadfile)

encryptedtext = "JELBEEOLZRNJEEAEEHOEJKOEOUNTNNLJAEFEOETJEEAJEATEEAWLTHKTESARIZTBTNNEELLOEEEATITDLNEEDJOATTLNESEONOHNTELIOETNEEAJEATEEAWLTHKTESWOLKODKOPLTENDNTNOHOEZENEJGINORZREDAETNSMOUEENNEELLOEEEATITDIRMEKGOLNAEIGLMJVNVJIIOVNEEINIKLLLANNLRNONRGOATGTVNAAEEEWTNVELEENEUGJELORJEZIUIIAEVNNATZISAONETNENCEIGLPNGIEVNRGOATGTVNAAEEEWTKWEIMIAJOATTLNESEONOHNTELIKOEOUNTNNLJAEFEOETJEUGJELORJEZIUIIZVOHJEKOIADRNEELNEETLNNEELLOEEEATITDLNEEDNANDMNETNEEWDWHNEEEOEITEIOPLTENDNTNOHOEZENEJGINORZREDAETNSMOUEENLOVENANDMNETNEEWDWHNEIETELUMATZISAONETNENCEIGLPIOVNEEINIKLLLANNLRNOOPLTENDNTNOHOEWEETJENNGSATVNEWOLKODKOPLTENDNTNOHOEZENEJKKLRJBRHGNNEAIELNEETVEJDEATZISAONETNENCEIGLPIOVNEEINIKLLLANNLRNOZNGPKKLRJBRHGNNEAIELNEEEHOEJKOEOUNTNNLJAEFEOETJEUGJELORJEZIUIIAEVNNATZISAONETNENCEENNEIRIVEWNKAKRIOLMEEEUGJELORJEZIUIIAEVNNEAATNELEENWINSNEHNMHONEBZJOATTLNESEONOHNTELIKOEOUNTNNLJAEFEOETJEAOEGEAATNELEENWINSNEHNGROEDKGINORZREDAETNSMOUEENNEELLOEEEATITDLNEEDJOATTLNESEONOHNNEIBNLKEEIKGEANGROEDKGINORZREDAETNSMOUEENNLETRENZNELEAESGPLAKEDLOIOVNEEINIKLLLANNLRNOOPLTENDNTNOHOEZENEJOVZJNNLETRENZNELEAESGPIOLMEEEUGJELORJEZIUIIAEVNNATZISAONETNENCEIGLPIOVNEEINIKLLLANGMEETSEDTKDJNNIETELUMATZISAONETNENCEIGLPWEZHPJVOEBTERNNPAESAMGAIMKOEOUNTNNLJAEFEOETJEUGJELORJEZIUIIAEVNNIEAEWEZHPJVOEBTERNNPAELNEETLNNEELLOEEEATITDLNEEDJOATTLNESEONOHNTELIKOEOUNTNNLJAEFEEDFNDEEIIAIEEDKWEIMIAJOATTLNESEONOHNTELIELOAIEEMGIEBADNEALJGEMTNTGINORZREDAETNSMOUEENNEELLOEEEATITDLNEEDTNLOELOAIEEMGIEBADNEALJVNVJIIOVNEEINIKLLLANNLRNOOPLTENDNTNOHOEZENEJGINORZREDAETNSM"
encryptedtext.lower()
key = [3, 4, 2, 1, 0, 5, 6, 7]

print(columnar_decoder(encryptedtext,key))



amount = {i:len(encryptedtext)//len(key) for i in key}
for i in range(len(encryptedtext)%len(key)):
    amount[key[i]]+=1

rows = {i:[] for i in key}

total = 0
for i in sorted(rows):
    for _ in range(amount[i]):
        rows[i].append(encryptedtext[total])
        total += 1

string_ints = [str(int) for int in key]
print(" ".join(string_ints))
for i in range(math.ceil(len(encryptedtext)/len(key))):
    for row, value in rows.items():
        if len(rows[row])>i:
            print(f"{value[i]} ",end="")
    print()

#print(fitness_key([3, 4, 0, 2, 1, 5, 6, 7],encryptedtext,defaultquadgramarray))

"""
neighbours = getNeighbours(key)

print(len(neighbours))
best = []
for i in neighbours:
    decoded = columnar_decoder(encryptedtext,i)
    fitness = fitness_key(i,encryptedtext,defaultquadgramarray)
    best.append([fitness,i,decoded])

best = sorted(best)

for i in range(40):
    print(f"{best[i][0]} {best[i][1]} {best[i][2]}")
    print()
"""
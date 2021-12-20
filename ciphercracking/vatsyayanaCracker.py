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


def vatsyayana_decode(text:str,key:dict):
    result = ""
    for char in text:
        result+= key[char]
    return result



def generate_key():
    letters = list("abcdefghijklmnopqrstuvwxyz")

    key = {}
    for _ in range(13):
        first = random.choice(letters)
        letters.remove(first)

        second = random.choice(letters)
        letters.remove(second)

        key[first] = second
        key[second] = first
    return key


def key_to_list(key):
    listkey = []
    
    keys = list(key.keys())
    vals = list(key.values())
    for i in range(0,26,2):
        listkey.append(keys[i])
        listkey.append(vals[i])
    return listkey


def keylist_to_key(keylist):
    keydict = {}
    for i in range(0,26,2):
        keydict[keylist[i]] = keylist[i+1]
        keydict[keylist[i+1]] = keylist[i]
    return keydict


def generate_neighbours(key):
    neighbours = []
    keylist = key_to_list(key)

    for i in range(26):
        for j in range(26):
            newkey = keylist.copy()
            newkey[i],newkey[j] = newkey[j],newkey[i]
            neighbours.append(keylist_to_key(newkey))
    return neighbours


def fitness_key(key:dict,encryptedtext:str,defaultquadgram):
    decoded = vatsyayana_decode(encryptedtext,key)
    return calculate_error_text(decoded,defaultquadgram)


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
    neighbours = generate_neighbours(currsolution)
    
    bestneighbour,bestneighbourfitness = getBestNeighbour(neighbours,encryptedtext,defaultquadgram)

    while bestneighbourfitness < currfitness:
        currsolution = bestneighbour
        currfitness = bestneighbourfitness
        neighbours = generate_neighbours(currsolution)
        bestneighbour,bestneighbourfitness = getBestNeighbour(neighbours,encryptedtext,defaultquadgram)

    return currsolution,currfitness


with open("default_quadgram.pkl", "rb") as quadfile:
    defaultquadgramarray = pickle.load(quadfile)


encryptedtext = "AKITDSIENIZIEDEANEHNAORKNRETWNTISHVJAAEELUELSHAKBATIEWLTILNUINHRKDPEKSTOENRNEODBEAZEAKBENONKDLGRKDPEKSTOENRNANLAAEEAENOWWINTETNRNIAAKIAMNHHEAEOAITEAEEATRNANKUOEANDGWDANEIBVJAAEELUELSHHOARTEAHSKRTEEAKBEEBVJAAEELUELSHKTDUIWICAAGETETFAAWOTLLANICETLLTARLERSAAPNSUNNKTLDWIPTRDENSWRKAOAITEAEEATRNGRECJITKDMIJISKRTELGOAITEAEEATRNWIDIAZANKIELUIHILEIERNATEANDINAAUELUELSHEOPNDIWICNMANIPHLALKGWISTOENRNLERSAAJIEHOTZDMEHOTBEOEBESTOENRNLERSAARATNDTKTNWEEIATBDCEANRGWICTIISSSRTEEATRNENMATERAAREKTIETEADDTTELUELSHEOPNDIILMAGRTALREGRDMEHOGILUELSHEOPNDINIARRNEATTEOASWRSWINIETRANAEIOONTVPNSUNNNDNSRKNIWBEEAIAOOWTIDEEEEATRNENMATEEVTLWLATINIWLLREGRBEEEATRNENMATEAKUENONIALNNWTEKATKTLOAUEAIAKINTSCENMATERKDPEKAKUAENIKOENPAOUAKEOPNDIIUNEEAAFENEVDOZANEVOIEILELEOPNDIIUNEEAAKNSAARHNIAZTTTEEBHEADDAAKHNSLCCMDTNDNSRKVJAAEEKNICZHNLNETNDENHTENMATERKDPEKKDDAEBTCFILEBZANEVIEENMATERKDPEKIENDZGNRNDNNNVAETAKOERAKNARTETTAGEPSESWGOAITEAIEIATNREAENAIKERNNDNSRKVJAAEEBEIAIGLINASIGFILEBELNDNSRKVJAAEEEAATNAKIRRKIULMDTKLDANEIEWIRONNNTSTOENRNLERSAAEAITAKLAAKILELAIWPSESWGOAITEATEETEWETBEOEINASIGIIPSESWGOAITEANRNLEKNIHOIKEERTINIERDSHNLAKEWDEERKDPEKSTOENRNNRTSKNNRTILPEEDGIUNEEAAPSESWGIGEKDNSNONKDSUGCFEBIUNEEAAPSESWGHNKIJAKHAAINKEATARIRNALNIKHDWAAEAIUNEEAAPSESWGHNNAAKONGINTMILRUPNSUNNNDNSRKEBDHFEJSUGCFEINIWLGIPNSUNNNDNSRKEANSZRALCDWNWTEANANIADSKTINUNDDDMEOPNDIIUNEEAAEAEIRAEAAWNATWNJDLERSAAPNSUNNWLRILAIOIEILKDMIJIEELERSAAPNSUNN"
encryptedtext = encryptedtext.lower()

while True:
    latestkey = generate_key()
    key,fitness = hillclim(latestkey,encryptedtext,defaultquadgramarray)
    decoded = vatsyayana_decode(encryptedtext,key)
    print(f"{round(fitness,5)} {key} {decoded[:min(len(decoded),1000)]}")

    userin = input("try again (Q = quit)")
    if userin.lower() == "q":
        break
    



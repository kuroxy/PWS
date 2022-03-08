from collections import Counter
import enigma_cy
import time
import math
import pickle

#hill climbing

with open("default_quadgram.pkl", "rb") as quadgramfile:
    defaultquadgramarray = pickle.load(quadgramfile)
    

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



def fitness_plugboard(plugboard,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram):
    decoded = enigma_cy.encode_enigma(plugboard, rotors, offsets, turnovers, reflector, encryptedtext)
    return calculate_error_text(decoded,defaultquadgram)



def getNeighbours(plugboardlist):
    fulllist = []
    for i in range(26):
        inew = plugboardlist.copy()
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



def getBestNeighbour(plugboards,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram):
    bestfitness = math.inf
    bestkey = None
    for plugboard in plugboards:
        currfitness = fitness_plugboard(plugboard,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram)
        if currfitness < bestfitness:
            bestfitness = currfitness
            bestkey = plugboard
            
    return bestkey,bestfitness
 

def hillclim(plugboard,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram):
    currsolution = plugboard
    currfitness = fitness_plugboard(plugboard,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram)
    neighbours = getNeighbours(currsolution)
    
    bestneighbour,bestneighbourfitness = getBestNeighbour(neighbours,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram)


    while bestneighbourfitness < currfitness:
        currsolution = bestneighbour
        currfitness = bestneighbourfitness
        neighbours = getNeighbours(currsolution)
        bestneighbour,bestneighbourfitness = getBestNeighbour(neighbours,rotors,offsets,turnovers,reflector, encryptedtext,defaultquadgram)
    return currsolution,currfitness


def crackplugboard(rotorlist,offsetlist,turnoverlist,reflw,text,defaultquadgramarray):
    startingplugboard = enigma_cy.create_plugboard("")
    hillclimbplug = hillclim(startingplugboard,rotorlist,offsetlist,turnoverlist,reflw,text,defaultquadgramarray)

    return [hillclimbplug[0],enigma_cy.encode_enigma(hillclimbplug[0], rotorlist, offsetlist, turnoverlist, reflw, text)]



def crackrotorsoffset(rotorchoices,turnoverchoices,reflw,text,printStatus=False,allowDuplicateRotors=False):
    best=[]
    startingplugboard = list(range(26))
    for i in range(len(rotorchoices)):
        for j in range(len(rotorchoices)):
            for k in range(len(rotorchoices)):
                if (i != j and j != k and i != k) or allowDuplicateRotors:

                    rotorlist = [rotorchoices[i],rotorchoices[j],rotorchoices[k]]
                    turnoverlist = [turnoverchoices[i],turnoverchoices[j],turnoverchoices[k]]

                    a = enigma_cy.crack_offset(startingplugboard, rotorlist, turnoverlist, reflw, text)
                    a.sort(key = lambda x: -enigma_cy.IoC(x[1]))

                    best.append([enigma_cy.IoC(a[0][1]),[i,j,k],a[0][0],a[0][1]])
                    
                    if printStatus:
                        print(f"Tested rotors:{[i,j,k]} offset:{a[0][0]} IoC:{best[-1][0]}")
    best.sort(key = lambda x: -x[0])
    return best












# defaults



rotorIw = [ord(i)-65 for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
turnoverI = enigma_cy.char_to_val("Q")

rotorIIw = [ord(i)-65 for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
turnoverII = enigma_cy.char_to_val("E")

rotorIIIw = [ord(i)-65 for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
turnoverIII = enigma_cy.char_to_val("V")


reflectorBw = [ord(i)-65 for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]



rotors = [rotorIw,rotorIIw,rotorIIIw]
turnovers = [turnoverI,turnoverII,turnoverIII]
reflw = reflectorBw

# settings

if __name__ == '__main__':
    text = "JURADMAISTRGKMMKFQEPPZOXIHIKHHUGNPGCDVWPZGQFZXMCPGJFTYLVKIPGSAFOJQRFMBGFTZSRYWVOVEZBEKMGCICEZGAHMMPYMAXLWKZZSUH"
    text = text.lower()



    res = crackrotorsoffset(rotors,turnovers,reflw,text)
    for i in res:
        print(i)


    print("------")
    rotorlist = [rotors[2],rotors[0],rotors[1]]
    turnoverlist= [turnovers[2],turnovers[0],turnovers[1]]
    offsetlist = [1,2,3]

    for i in crackplugboard(rotorlist,offsetlist,turnoverlist,reflw,text,defaultquadgramarray):
        print(i)
    



#http://www.cs.cornell.edu/courses/cs3110/2019sp/a1/#step-5-enigma-tutorial
def makeplugboard(plug):
    returndict = {}
    for i in range(0,len(plug),2):
        a = char_to_val(plug[i])
        b = char_to_val(plug[i+1])

        returndict[a] = b
        returndict[b] = a
    return returndict


def char_to_val(char):
    return ord(char.upper())-65


def val_to_char(val):
    return chr(val+65)


def w(rotor, offset ,letter):
    inchar = letter+offset  
    return (rotor[inchar%26]-offset)%26


def winverse(rotor, offset ,letter):
    outchar = (letter+offset)%26
    return (rotor.index(outchar)-offset)%26


def plugboardswitch(plugboard,char):
    return plugboard[char] if char in plugboard else char


class rotor:
    def __init__(self, rotorwiring):
        self.rotorwiring = [ord(i)-65 for i in rotorwiring]
        self.offset = 0
        self.turnover = 0

    def w(self, val):
        inchar = val+self.offset  
        return (self.rotorwiring[inchar%26]-self.offset)%26

    def winv(self, val):
        outchar = (val+self.offset)%26
        return (self.rotorwiring.index(outchar)-self.offset)%26

    def set_turnover(self,val):
        if type(val) is str:
            val = char_to_val(val)
        self.turnover = val
    
    def set_offset(self,val):
        if type(val) is str:
            val = char_to_val(val)
        self.offset = val

    def step(self):
        self.offset += 1
        self.offset%=26


def cipher_char(plugboard, rotors, reflector, char) -> int:
    if type(char) is str:
        val = char_to_val(char)

    temp = plugboardswitch(plugboard,val)

    for rotor in rotors[::-1]:
        temp = rotor.w(temp)

    temp = reflector.w(temp)

    for rotor in rotors:
        temp = rotor.winv(temp)

    return plugboardswitch(plugboard,temp)


def step_rotors(rotors):
    
    steps = [0 for _ in range(len(rotors))]
    steps[-1]=1
    for rindex in range(1,len(rotors)):
        
        if rotors[rindex].offset == rotors[rindex].turnover:
            
            steps[rindex] = 1
            steps[rindex-1] = 1

    for i in range(len(rotors)):
        if steps[i]:
            rotors[i].step()


def encode_enigma(plugboard, rotors, reflector, string):
    encoded = ""
    for char in string:
        step_rotors(rotors)
        encoded += val_to_char(cipher_char(plugboard, rotors, reflector, char))
    return encoded

def printrotoroffset(rotors):
    offsets = "".join(val_to_char(rotor.offset) for rotor in rotors)
    print(offsets)

# defaults


rotorI = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ") 
rotorI.set_turnover("Q")

rotorII = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE") 
rotorII.set_turnover("E")

rotorIII = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO") 
rotorIII.set_turnover("V")

reflectorB = rotor("YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflectorC = rotor("FVPJIAOYEDRZXWGCTKUQSBNMHL")

#settings


# left to right so index 0 is the most left
rotorlist = [rotorIII,rotorII,rotorI]

rotorlist[0].set_offset("A")
rotorlist[1].set_offset("A")
rotorlist[2].set_offset("A")

#reflector used
refl = reflectorB


plugboardletters = ""


# 
plugboard = makeplugboard(plugboardletters)

text = "MTNCZRBKEPJDRNU"

enc = encode_enigma(plugboard,rotorlist,refl,text)
print(text)
print(enc)
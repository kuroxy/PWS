
cpdef IoC(str text):
    cdef float counter[26]
    counter[:] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cdef float total = 0
    cdef int i

    for i in range(len(text)):
        c = text[i].lower()
        if c in "abcdefghijklmnopqrstuvwxyz":
            counter[char_to_val(c)] +=1
            total+=1

    cdef float ic = 0
    for i in range(26):
        ic += (counter[i]/total)*((counter[i]-1)/(total-1))
    return ic


cpdef create_plugboard(str plugs):
    cdef list returnlist = [i for i in range(26)]

    cdef int i 
    for i in range(0,len(plugs),2):
        a = char_to_val(plugs[i])
        b = char_to_val(plugs[i+1])
        returnlist[a] = b
        returnlist[b] = a
    return returnlist


cpdef val_to_char(int val):
    return chr(val+65)


cpdef char_to_val(str c):
    return ord(c.upper())-65


cpdef w(list rotorwiring,int offset, int val):
        return (rotorwiring[(val+offset)%26]-offset)%26


cpdef winv(list rotorwiring,int offset, int val):
    return (rotorwiring.index((val+offset)%26)-offset)%26


cpdef cipher_char(list plugboard, list rotorwires,list offsets, list reflectorwire,str c):
    cdef int val = char_to_val(c)

    val = plugboard[val]

    for rindex in range(3):
        val = w(rotorwires[2-rindex],offsets[2-rindex], val)

    val = w(reflectorwire,0, val)

    for rindex in range(3):
        val = winv(rotorwires[rindex],offsets[rindex], val)
    

    return val_to_char(plugboard[val])


cpdef step_rotors(list offsets, list turnovers):
    cdef int steps[3]
    steps[:] = [0,0,1]

    cdef list newoffset = offsets.copy()
    cdef int rindex
    for rindex in range(1,3):
        if offsets[rindex] == turnovers[rindex]:
            steps[rindex] = 1
            steps[rindex-1] = 1

    for rindex in range(3):
        if steps[rindex]:
            newoffset[rindex] += 1
            newoffset[rindex] %=26

    return newoffset






cpdef encode_enigma(list plugboard, list rotorwires,list offsets,list turnovers, list reflectorwire,str text):
    cdef str encoded = ""
    cdef int i
    for i in range(len(text)):
        offsets = step_rotors(offsets, turnovers) # step
        encoded += cipher_char(plugboard, rotorwires, offsets, reflectorwire, text[i])
    
    return encoded





def crack_offset(list plugboard, list rotorwires,list turnovers, list reflectorwire,str text):
    
    bestrotor = []
    cdef int i
    cdef int j 
    cdef int k

    for i in range(26):
        for j in range(26):
            for k in range(26):
                bestrotor.append([[i,j,k],encode_enigma(plugboard, rotorwires,[i,j,k],turnovers, reflectorwire, text)])
                
    return bestrotor



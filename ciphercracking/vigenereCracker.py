from collections import Counter
import enum
import re
import CaesarCracker 


def repeated(text: str, offset: int):
    return sum(char == text[(i+offset)%len(text)] for i,char in enumerate(text))
    

def crackkeylength(text:str,keyrange:int,debug=False) -> dict:
        
    repeatedlist = [repeated(text,i) for i in range(keyrange*10)]

    if debug:
        for i in range(len(repeatedlist)):
            print("-"*(repeatedlist[i]//10))

    keylengths = {}
    for keylen in range(1,len(repeatedlist)//10):
        peaks=0
        total=0
        for i in range(2,len(repeatedlist)):
            if i%keylen==0:
                peaks+=repeatedlist[i]
                total+=1
        keylengths[keylen] = peaks/total
        #print(f"{keylen}: {peaks/total}")

    return dict(sorted(keylengths.items(), key=lambda item: -item[1]))


def splittext(text:str,keylength:int):
    result = ["" for _ in range(keylength)]
    for index, char in enumerate(text):
        result[index%keylength]+=char
    return result


text = """nwkbcjfhbpvxvrmbqsexbstbzvvknslkkkhvdchkhosedozvckfvgxoutdvvmqoctmhzlmvbxsnvkbwadsgmxbbzxdwxwxsvfdhyxpwildciwofyxdcgssqyhwrfhbhvzkoepkoiaohmhbwxxuszsofibtyjmydkxnswhmijbxrvsohibvcxbozzzdcgdizfkobvgbspdizfkobzlnsxxfoceobqhybmtxvrgccchobcxsofkqoetnwvhywkzohitsbupofuwycieeyvlumntvyvk"""



keylengths = crackkeylength(text,25)
print(list(keylengths.keys()))
bestkey = list(keylengths.keys())[:5]
print(bestkey)

inputkeyleng = int(input("keylength: "))

split = splittext(text,inputkeyleng)

keys = []
solvedsplit=[]
for i in split:
    solve= CaesarCracker.caesar_cracker(i)
    keys.append(list(solve.keys())[0])
    solvedsplit.append(solve[list(solve.keys())[0]])

print(keys)
translatedkey = "".join(chr(97+num) for num in keys)
print(translatedkey)
decoded = "".join(solvedsplit[i % inputkeyleng][i // inputkeyleng] for i in range(len(text)))


print(decoded)
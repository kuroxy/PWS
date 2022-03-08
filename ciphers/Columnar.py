from math import ceil
import sys



def columnar_encode(text:str,key:list):
    text = text.lower()
    text = ''.join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz"])

    rows = {i:[] for i in key}

    for idx, letter in enumerate(text):
        row = key[idx%len(key)]
        rows[row].append(letter)


    rows = dict(sorted(rows.items()))

    return "".join("".join(value) for li, value in rows.items())



if __name__ == '__main__':
    
    text = """ditisvoorbeeldvancolumnartranspositioncipherdezeiswellastigomtekrakenomdathetwerktopbigram"""
    key = "4,3,5,1,2,0"
    #4,3,5,1,2,0

    if len(sys.argv)>1:
        key = sys.argv[1]
        with open(sys.argv[2], "r", encoding="utf8") as file:
            text = file.read()


    key = key.lower()
    key = key.split(",")


    result = columnar_encode(text,key)
    print(result)

    if len(sys.argv)>3:
        with open(sys.argv[3], 'w',encoding="utf-8") as f:
            f.write(result)
        print("done")


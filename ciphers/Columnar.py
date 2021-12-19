from math import ceil
import sys
COUNTED = "abcdefghijklmnopqrstuvwxyz"

text = """"""
key = "7,4,3,5,6,1,2,0"
#4,3,5,1,2,0


if len(sys.argv)>1:
    key = sys.argv[1]
    with open(sys.argv[2], "r", encoding="utf8") as file:
        text = file.read()


key = key.lower()
key = key.split(",")

text = text.lower()
text = ''.join([i for i in text if i in COUNTED])

rows = {i:[] for i in key}

for idx, letter in enumerate(text):
    row = key[idx%len(key)]
    rows[row].append(letter)


rows = dict(sorted(rows.items()))

result = "".join("".join(value) for li, value in rows.items())

print(result)

if len(sys.argv)>3:
    with open(sys.argv[3], 'w',encoding="utf-8") as f:
        f.write(result)
    print("done")


import os

for i in range(26):
    os.system(f"python .\\frenquentieletters.py .\\texts\caesar\caesar{i}.txt .\\graphs\\caesar\\caesargraph{i}.png")
    #os.system(f'python .\ciphers\Caesarcipher.py {i} .\\texts\\formatnl.txt .\\texts\\caesar\\caesar{i}.txt')
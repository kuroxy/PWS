import matplotlib.pyplot as plt
   
Country = ['USA','Canada','Germany','UK','France']
GDP_Per_Capita = [45000,42000,52000,49000,47000]


counter = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
total = 0

with open("texts\\sample.txt", "r", encoding="utf8") as file:
    for line in file:
        for c in line:
            c = c.lower()
            if c in counter:
                counter[c]+=1
                total+=1


print(counter)
for letter in counter:
    counter[letter]/=total

letters = [*counter]# a,b,c,d,e,,,
kansen = list(counter.values())

plt.bar(letters,kansen) 
plt.title('Frequentie van letters')
plt.xlabel('Letter')
plt.ylabel('Kans')
plt.show()
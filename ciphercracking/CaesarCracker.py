from collections import Counter


def countmonograms(text):
    text = text.lower()
    counter = [i for i in text if i in "abcdefghijklmnopqrstuvwxyz"]
    total = len(counter)
    counter = dict(Counter(counter))

    for comb in counter:
        counter[comb]/=total
    return counter


def caesar_decoder(text,key):
    return "".join(chr((ord(i) -key - 97) % 26 + 97) for i in text)



def caesar_cracker(text:str) -> dict: # {key:decodedwithkey}
    encryptedtext = text.lower()

    monogram = countmonograms(encryptedtext)
    monogram = dict(sorted(monogram.items(), key=lambda item: -item[1]))
    
    result = {}
    for char in monogram:
        key = (ord(char) - ord("e"))%25
        result[key]=caesar_decoder(encryptedtext,key)
    return result

if __name__ == '__main__':
    encryptedtext = "vqhdmmsfaruwluztqnuzqqzeusmdqftqfuefiqqggdezmotfeiqxussqzabnqpuzqqztafqxuzqqzefmpimmdzuqymzpazetaadfimmdzuqymzpazewqzfqzzuqymzpazeefaadfabpqhxaqdxusfqqzxqsqrxqeiuvzqzwxqpuzsefgwwqzpuqhmzvagaryuvwgzzqzluvzqqzeotqyqduzspqdmpualmotfqzpqlqzmotftqqrfmxxqeimfuwhmzqqzzmotfhqdimotftqfueqqzzmotfpuqvqzadymmxmxxqqzuzruxyeluqftqfueqqzzmotfpuqiadpfnqlazsqzuztqfyaauefqxuqptqfueqqzzmotfimmdhmzuwpmotfpmfuwtqyzaaufnqxqhqzlagymmdhmzzmotfnqxqqruwtqyyqfvagatatuwnqzzasimwwqdqzuwefmmdzmmdtqfbxmrazpqzuwpqzwmmzpqpmsxmzssqxqpqznqsaztqflaymmdqdhmzpaadsmmzyqfvagzuqfiqfqzpimmdpqdquequzpusqzlagzgxusuwtuqduzqqziuxphdqqypqefmpqztqnzqfpqzmotfhmzyqzxqhqzsqtmpymmdtqxmmeqdwayfiqqdxuotfpaadpqdmyqztaqiqxhaadazepqiqdqxphmzzmotftqqrfefuxsqefmmz"
    encryptedtext = encryptedtext.lower()

    print(caesar_cracker(encryptedtext))





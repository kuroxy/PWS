#https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4

def encode_Vigenere(plaintext, key):
    plaintext = plaintext.lower()
    plaintext = ''.join([i for i in plaintext if i in "abcdefghijklmnopqrstuvwxyz"])
    plaintext = plaintext.upper()

    key = key.upper()

    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 97)
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    ciphertext = ''.join([i for i in ciphertext if i in "abcdefghijklmnopqrstuvwxyz"])
    ciphertext = ciphertext.upper()

    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)
    return plaintext


if __name__ == '__main__':
    print(encode_Vigenere("okke","abcd"))
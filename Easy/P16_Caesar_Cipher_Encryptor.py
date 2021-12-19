def caesarCipherEncryptorMy(s, n):
    res = ""
    for i in s:
        if ord(i) + n > 122:
            res += chr(96 + (ord(i) + n) % 122)
        else:
            res += chr(ord(i) + n)
    return res


print(caesarCipherEncryptorMy("xyz", 2))


# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letters.append(getNewLetter(letter, new_key))
    return "".join(new_letters)


def getNewLetter(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)


print(caesarCipherEncryptor("xyz", 2))


# O(n) time | O(n) space
def caesarCipherEncryptor2(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        new_letters.append(getNewLetter2(letter, new_key, alphabet))
    return "".join(new_letters)


def getNewLetter2(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    return alphabet[new_letter_code] if new_letter_code <= 25 else alphabet[-1 + new_letter_code % 25]


print(caesarCipherEncryptor2("xyz", 2))

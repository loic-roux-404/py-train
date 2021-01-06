#!/usr/bin/python3

# Hamming
def Hamming(a, b):
    if type(a) != str or type(b) != str:
        raise Exception('Need string')

    if len(a) != len(b):
        raise Exception("String length differ")

    distance = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            distance += 1

    return distance


print(Hamming("400", "340"))
print(Hamming("444", "244"))

# Anagram
def isSame(str1, str2):
    # Loop an array of bytes, ex : [35, 40, 34]
    for i in list(bytes(str1.lower().encode('utf8'))):
        if i not in list(bytes(str2.lower().encode('utf8'))):
            return False
    for i in list(bytes(str1.lower().encode('utf8'))):
        if i not in list(bytes(str2.lower().encode('utf8'))):
            return False
    return True

def anagram(a, b):
    if type(a) != str or type(b) != str:
        raise Exception('Need string')

    if len(a) != len(b):
        raise Exception("String length differ")

    return isSame(a, b)

print(anagram('Logan', 'Ligon'))
print(anagram('Logan', 'Lagon'))

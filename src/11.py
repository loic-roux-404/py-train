def mxysqgzo(limit = 10000):
    for n in range(1, limit):
        somme = 0
        for letter in list(str(n)):
            letter = int(letter)
            somme += letter ** letter
            if somme == n:
                print(somme, n)
                break

mxysqgzo()

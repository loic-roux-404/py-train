#!/usr/bin/env python
# ======
# titre
# role
# entrée
# sortie
# (optionel)
# Saisie
# initialisation
# Affichage
# ======
enablePrompts = False

if(enablePrompts):
    n = int(eval(input("bit compare :")))

    if (not (n & 1)):
        print('pair')
    else:
        print('impair')

    print('\nFor')
    for v in range(1, n, 2):
        print('z', v)

    x = eval(input("\nwhile :"))
    while n + 1 <=x:
        n+=1

    print("\nranges :", n)
    # nested
    for i in range(1, 11):
        print("table de", i)
        for j in range(1, 11):
            print("\t", j, "*", i, "=", j*i)

print('\ntuple')
TupleEx = (2.718, 2.14)
print(TupleEx)

print('\nlist')
listEx = []
listEx.append(1)
print(listEx)

print('\nlist sort')
# [expression for x in sequence if conditionnelle]
t = (11, 22, 33)
print(2**)

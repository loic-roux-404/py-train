from tests import run

# Palindrome
def is_palindrome(n):
    initial_nb = n
    # Nombre initial à retrouver
    check_pal_nb = 0
    while (n > 0):
        # On calcule le chiffre correspondant en testant le résultats de ses division apr dix
        chiffre = n % 10
        # Comptez le nombre de palindrome et utiliser une relation propotionnelle
        # afin de retrouver le nombre initial pouvant être un palindrome
        check_pal_nb = check_pal_nb * 10 + chiffre
        # On passe au niveau en dessous 9999 --> 999
        # Ainsi à la prochaine itération on peu vérifier que les chiffres son bien
        # divisible pat des dizaine
        n = n // 10

    # Si notre nombre possède un nombre de palindrome égal
    if(initial_nb == check_pal_nb):
        return True
    else:
        return False

print(is_palindrome(999999))

def million_test():
    count = 0
    for i in range (1, ):
        if is_palindrome(i):
            count += 1

# million_test()

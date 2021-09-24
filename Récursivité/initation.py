def somme(n):
    if n == 0:
        return 0
    else:
        return n + somme(n-1)


def power(x: int, n: int) -> int:
    """
    Calcule la puissance selon la méthode chelou du prof
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return x * power(x, n-1)


def factorio(n):
    m = 1
    if n == 0:
        return 1
    else:
        return n*factorielle(n-1)
    return m


def boucle(i, k):
    if k == i:
        return print(i)
    else:
        print(i, end="\n")
        boucle(i+1, k)
boucle(1, 10)


def nb_chiffres(n):
    if n<10:
        return 1
    else:
        return 1 + nb_chiffres(n//10)


def new_chiffre(n):
    return len(str(n))


def palindrome(s):
    k1=0
    k2=len(s)
    if s[k1] == s[k2]:
        s.pop()
        s.pop(0)
        return palindrome(s)
print(nb_chiffres(256738648245573256))
print(new_chiffre(256738648245573256))

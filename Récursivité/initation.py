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


def palindrome(s: str) -> None:
    ls = []
    for i in range(s):
        ls.append(i)
    k1=0
    k2=len(ls)-1
    if ls[k1] == ls[k2]:
        ls.pop()
        ls.pop(0)
        print("{} = {}".format(ls[k1], ls[k2]))
        s=""
        for i in range(ls):
            s += i
        return palindrome(ls)
print(nb_chiffres(256738648245573256))
palindrome("kayak")

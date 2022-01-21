import time
from random import randint


def recherche(tab:list, val: int):
    """Recherche un nombre dans un tableau"""
    i = 0
    while tab[i] != val:
        i += 1
    return True


def dichotomie_recur(tab: list, val: int):
    """Recherche dichotomique d'un nombre dans un tableau"""
    if len(tab) == 0:
        return False
    else:
        milieu = len(tab) // 2
        if tab[milieu] == val:
            return True
        elif tab[milieu] > val:
            return dichotomie_recur(tab[:milieu], val)
        else:
            return dichotomie_recur(tab[milieu:], val)


def dichotomie_iter(tab: list, val: int):
    """Recherche dichotomique d'un nombre dans un tableau. Version Itérative"""
    deb = 0
    fin = len(tab) - 1
    milieu = int((deb + fin) / 2)
    while deb <= fin:
        if tab[milieu] == val:
            return True
        elif tab[milieu] > val:
            fin = milieu - 1
        else:
            deb = milieu + 1
        milieu = int((deb + fin) / 2)
    return False



if __name__ == "__main__":
    tab = [randint(1, 100000000) for i in range(1, 100000000)]
    tab.sort()
    start = time.time()
    print(dichotomie_recur(tab, 356984))
    print("En récursif : {}".format(time.time() - start))
    start = time.time()
    print(dichotomie_iter(tab, 356984))
    print("En itératif : {}".format(time.time() - start))
    start = time.time()
    print(recherche(tab, 356984))
    print("En recherche : {}".format(time.time() - start))
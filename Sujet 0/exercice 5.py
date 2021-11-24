def convertir(T: list) -> int:
    """
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et représentatn un entier écrit en binaire.
    Renvoie l'écriture décimale de l'entier positif dont la représentation binaire est donnée par le tableau T.
    """
    n = 0
    for i in range(len(T)):
        n += T[i]*2**(len(T)-i-1)
    return n

if __name__ == '__main__':
    assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
    assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130
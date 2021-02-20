def tri(T: list, cle: str) -> list:
    """
    Fonction qui renvoie un tableau trié selon une clé définie en paramètre
    le tableau est vide en cas d'erreur de clé
    :param T: le tableau de départ
    :param cle: la clé de tri
    :return: une liste
    """

    tab = []
    if cle == "debut":
        tab = sorted(T, key=lambda x: x[1])
    elif cle == "fin":
        tab = sorted(T, key=lambda x: x[2])
    elif cle == "duree":
        for i in range(len(locations)):
            tmp_1 = locations[i][1]
            tmp_2 = locations[i][2]
            int(tmp_1)
            int(tmp_2)
            tmp = tmp_2 - tmp_1
            locations[i].append(tmp)
        tab = sorted(T, key=lambda x: x[3])
    else:
        tab = []
    return tab


def Camion_occupe(jour: int) -> bool:
    pass
    if freetruck is True:
        findloc(jour)
        freetruck = False
    else:
        jour += 1
        freetruck = True
    return freetruck


def findloc(jour: int):
    pass


freetruck = True
locations = [[1, 1, 8], [2, 2, 5], [3, 4, 7], [4, 1, 3], [5, 5, 9], [6, 8, 11],
             [7, 9, 10], [8, 13, 16], [9, 11, 14]]

# DEBUG: print all functions
print(tri(locations, "debut"))
print(tri(locations, "fin"))
print(tri(locations, "duree"))

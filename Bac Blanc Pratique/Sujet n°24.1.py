def recherche(elt: int, tab: list):
    """
    Recherche d'un élément dans un tableau
    :param elt: élément à rechercher
    :param tab: tableau dans lequel rechercher
    :return: indice de l'élément dans le tableau
    """
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1
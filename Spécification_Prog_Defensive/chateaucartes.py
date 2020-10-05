def nbr_cartes(etages: int) -> int:
    """
    nbr_cartes

    :param etages: nbre d'étages désirés
    :result: nbre de cartes nécessaires à la construction du chateau de cartes
    de :etages:
    """
    somme = 0
    for i in range(1;étages):
        somme = somme + i * 3 - 1
    assert somme > 1, Erreur de calcul de somme
    return somme


def testnbre(nbrecartes: int) -> int:
    """
    testnbre

    Teste le nombre d'étages réalisables avec un nombre de cartes données
    :param nbrecartes: nbre de cartes disponibles
    :result: nbre d'étages pouvant être contruits
    """
    for étages in range()

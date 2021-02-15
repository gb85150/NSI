def nbr_cartes(etages: int) -> int:
    """
    nbr_cartes

    :param etages: nbre d'étages désirés
    :result: nbre de cartes nécessaires à la construction du chateau de cartes
    de :etages:
    """
    assert etages >= 1, "le nombre d'étages doit être un entier positif"
    somme = 0
    for i in range(1, etages+1):
        somme = somme + i * 3 - 1
        numetage = i
    assert somme > 1, "Erreur de calcul de somme"
    return somme, numetage


def testnbre(nbrecartes: int) -> int:
    """
    testnbre

    Teste le nombre d'étages réalisables avec un nombre de cartes données
    :param nbrecartes: nbre de cartes disponibles
    :result: nbre d'étages pouvant être contruits
    """
    somme = 0
    compteur = 0
    while somme <= nbrecartes:
        compteur += 1
        somme = nbr_cartes(compteur)


testnbre(52)

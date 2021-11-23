def moyenne(liste: list) -> float:
    """
        moyenne(liste: list) -> float
        Entrée: un tableau non vide d'entiers
        Sortie: la moyenne des éléments du tableau de type float

    """
    return sum(liste) / len(liste)

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5
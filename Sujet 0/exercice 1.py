def recherche(liste:list, cible:int) -> list:
    """
    Fonction qui retourne la liste des indices où la valeur cible est présente dans la liste, Sinon retourne la longueur de la liste
    """
    x = False
    for i in range(len(liste)):
        if liste[i] == cible:
            x = i
    if not x:
        return len(liste)
    else:
        return x


print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))
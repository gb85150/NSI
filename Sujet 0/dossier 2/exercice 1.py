def moyenne(liste:list) -> float:
    """
    Soit un couple note / coefficient.
    Calcule la moyenne pondérée de la liste de couples
    """
    moyenne = 0
    for couple in liste:
        moyenne += couple[0] * couple[1]
    return moyenne / len(liste)


if __name__ == "__main__":
    # Test
    liste_notes = [(15,2),(9,1),(12,3)]
    print(moyenne(liste_notes))
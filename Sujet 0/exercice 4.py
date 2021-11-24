def dichotomie(tab, x):
    """
        tab : tableau trié dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # Cas du tableau vide
    if len(tab) == 0:
        return False, 1
    # Cas où x n'est pas compris entre les valeurs extrêmes
    if x < tab[0] or x > tab[-1]:
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return True
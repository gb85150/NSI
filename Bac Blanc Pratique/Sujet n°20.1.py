def est_palindrome(mot):
    """
        Vérifie si un mot est un palindrome
        :param mot: le mot à vérifier
        :type mot: str
        :return: True si le mot est un palindrome, False sinon
        :rtype: bool
    """
    if len(mot) == 1:
        return True
    if mot[0] == mot[-1]:
        return est_palindrome(mot[1:-1])
    else:
        return False

def nombre_est_palindrome(nombre):
    """
        Vérifie si un nombre est un palindrome
        :param nombre: le nombre à vérifier
        :type nombre: int
        :return: True si le nombre est un palindrome, False sinon
        :rtype: bool
    """
    return est_palindrome(str(nombre))
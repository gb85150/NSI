import random


def AddValueToDict(k, d, v, i):
    """
    k = key - d = dict - v = value - i = type value
    si le dictionnaire 'd' contient la clé 'k'
    on récupère la valeur
    """
    if k in d: i = d[k]
    # détermination du type de la valeur
    # si la valeur est de type set()
    if isinstance(i, set): i.add(v)
    # si la valeur est de type list()
    elif isinstance(i, list): i.append(v)
    # si la valeur est de type str()
    elif isinstance(i, str): i += str(v)
    # si la valeur est de type int()
    elif isinstance(i, int): i += int(v)
    # si la valeur est de type float()
    elif isinstance(i, float): i += float(v)
    # on met à jour l'objet 'i' pour la clé 'k' dans le dictionnaire 'd'
    d[k] = i
    # on retourne le dictionnaire 'd'
    return d


def ASCIIrandom_alea() -> dict:
    """
    Fonction qui construit un dictionnaire de codage
    à chaque lettre MAJUSCULE de l'alphabet on fait correspondre
    une lettre MAJUSCULE prise aléatoirement
    :return: un dictionnaire ex : {'A': 'D', 'B': 'Y'....}
    """
    ASCII = [chr(i) for i in range(65, 91)]
    ASCIIrandom = {}
    random.shuffle(ASCII)

    for i in range(0, 26):
        ASCIIrandom[chr(i+65)] = ASCII[i]
    return ASCIIrandom


def crypto_lettre(ASCIIrandom: dict, lettre: str) -> str:
    """
    Fonction qui renvoie une lettre cryptée d'après le dictionnaire associé
    :param ASCIIrandom:
    :param lettre: lettre MAJUSCULE
    :return: la lettre cryptée en MAJUSCULE
    """
    texte = ""
    for k in range(len(lettre)):
        if lettre[k] in ASCIIrandom.items():
            texte = texte + ASCIIrandom[lettre[k]]
        else:
            texte = texte + lettre[k]
    return texte


def crypto_texte(ASCIIrandom: dict, texte: str) -> str:
    """
    Fonction qui renvoie un texte crypté à partir du texte entré et
    du dictionnaire associé
    On utilise la fonction crypto_lettre
    :param dict:
    :param texte: texte en MAJUSCULES
    :return: le texte crypté en MAJUSCULES
    """
    pass


def lire_fichier(fichier: str) -> list:
    """
    Fonction qui renvoie une liste après lecture d'un fichier texte
    :param fichier:
    :return: liste contenant le texte
    """
    with open(fichier, "r") as fopen():
        liste = []
        liste = fopen.rstrip()
        return liste


def occurrence(texte: str) -> dict:
    """
    Fonction qui renvoie un dictionnaire composé des lettres de
    l'alphabet et du nombre d'occurences de la lettre dans le texte
    entré en paramètre
    :param texte: le texte crypté en MAJUSCULES
    :return: un dictionnaire
    """
    with open(encryptedfile, "r") as fopen():
        rstrip()
    pass


def maxi(ASCIIrandom: dict) -> str:
    """
    Fonction qui renvoie la lettre ayant la plus grande occurence
    des lettres du dictionnaire
    :param ASCIIrandom: dictionnaire des occurences
    :return: la lettre ayant la plus grande occurence
    """
    pass


def propose(texte: str) -> dict:
    """
    Fonction qui renvoie une proposition de dictionnaire de décodage
    du texte entré en paramètre
    On utilise les fonctions occurence et maxi
    :param texte:
    :return: le dictionnaire de décodage
    """
    pass


def permute(ASCIIrandom: dict, l1: str, l2: str) -> dict:
    """
    Fonction qui permute 2 lettres dans un dictionnaire
    :param ASCIIrandom:
    :param l1: lettre en MAJUSCULE
    :param l2: lettre en MAJUSCULE
    :return: le nouveau dictionnaire
    """


"""
#programme principal
table = lire_fichier("texte.txt")
d = propose(table)
print(d)
print(crypto_texte(d, table))
permute(d,"N","L")
permute(d,"H","B")
permute(d,"H","G")
permute(d,"L","U")
permute(d,"Q","H")
print()
print(crypto_texte(d, table))
"""
# DEBUG: use pass to disable
print(crypto_lettre(ASCIIrandom_alea(), "Bonjour, A B C".upper()))
print(lire_fichier(input("file path ? (including extension like .txt) : ")))

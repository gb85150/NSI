import random


def dico_alea() -> dict:
    """
    Fonction qui construit un dictionnaire de codage
    à chaque lettre MAJUSCULE de l'alphabet on fait correspondre
    une lettre MAJUSCULE prise aléatoirement
    :return: un dictionnaire ex : {'A': 'D', 'B': 'Y'....}
    """
    ASCII = [chr(i) for i in range(65, 91)]
    dic = {}
    random.shuffle(ASCII)
    for i in range(0, 26):
        dic[chr(i+65)] = ASCII[i]
    return dic


def crypto_lettre(dico: dict, lettre: str) -> str:
    """
    Fonction qui renvoie une lettre cryptée d'après le dictionnaire associé
    :param ASCIIrandom:
    :param lettre: lettre MAJUSCULE
    :return: la lettre cryptée en MAJUSCULE
    """
    return dico[lettre]


def crypto_texte(dico: dict, texte: str) -> str:
    """
    Fonction qui renvoie un texte crypté à partir du texte entré et
    du dictionnaire associé
    On utilise la fonction crypto_lettre
    :param dict:
    :param texte: texte en MAJUSCULES
    :return: le texte crypté en MAJUSCULES
    """
    t = ""
    for lettre in texte:
        if lettre in dico.keys():
            t += crypto_lettre(dico, lettre)
        else:
            t += lettre


# file write function
def lire_fichier(fichier: str) -> list:
    """
    Fonction qui renvoie une liste après lecture d'un fichier texte
    :param fichier:
    :return: liste contenant le texte
    """
    with open(fichier, "r") as fopen:
        # fopen.rstrip()
        liste = list()
        liste = fopen.readlines()
        return liste


def occurrence(texte: str) -> dict:
    """
    Fonction qui renvoie un dictionnaire composé des lettres de
    l'alphabet et du nombre d'occurences de la lettre dans le texte
    entré en paramètre
    :param texte: le texte crypté en MAJUSCULES
    :return: un dictionnaire
    """
    occurence = dict()
    for i in range(65, 91):
        occurence[chr(i)] = 0
    with open(texte, "r") as fopen:
        fopen.rstrip()
        fopen.upper()
        pass
    for lettre in texte:
        if lettre in occurence:
            occurence[lettre] += 1
        else:
            pass
    return occurence


def maxi(occurence: dict) -> str:
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
    pass


# programme principal
table = lire_fichier(input("file path ? (including extension like .txt) : "))
d = propose(table)
print(d)
print(crypto_texte(d, table))
permute(d, "N", "L")
permute(d, "H", "B")
permute(d, "H", "G")
permute(d, "L", "U")
permute(d, "Q", "H")

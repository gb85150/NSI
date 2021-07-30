import os
import platform
import csv


def clearconsole():
    command = 'clear'
    if platform.system() == 'Windows':  # If Machine is running on Windows, use cls
        command = 'cls'
    elif 'Linux' == platform.system() or 'Darwin' == platform.system() or 'Java' == platform.system():
        command = 'clear'
    os.system(command)


def printinfo():
    print("""
=====================================================================================================================
=====================================================================================================================
===       ___           ___           ___           ___           ___           ___       ___           ___       ===
===      /\  \         /\__\         /\  \         /\  \         /\  \         /\__\     /\  \         /\  \      ===
===     /::\  \       /:/  /         \:\  \       /::\  \       /::\  \       /:/  /    /::\  \       /::\  \     ===
===    /:/\:\  \     /:/  /           \:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \     /:/\ \  \    ===
===   /::\~\:\  \   /:/  /  ___       /::\  \   /:/  \:\  \   /:/  \:\  \   /:/  /    /::\~\:\  \   _\:\~\ \  \   ===
===  /:/\:\ \:\__\ /:/__/  /\__\     /:/\:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__\  ===
===  \/__\:\/:/  / \:\  \ /:/  /    /:/  \/__/ \:\  \ /:/  / \:\  \  \/__/ \:\  \    \/__\:\/:/  / \:\ \:\ \/__/  ===
===       \::/  /   \:\  /:/  /    /:/  /       \:\  /:/  /   \:\  \        \:\  \        \::/  /   \:\ \:\__\    ===
===       /:/  /     \:\/:/  /     \/__/         \:\/:/  /     \:\  \        \:\  \       /:/  /     \:\/:/  /    ===
===      /:/  /       \::/  /                     \::/  /       \:\__\        \:\__\     /:/  /       \::/  /     ===
===      \/__/         \/__/                       \/__/         \/__/         \/__/     \/__/         \/__/      ===
===                                                                                                               ===
===                                              CLASSROOM RESOLVER                                               ===
=====================================================================================================================
=====================================================================================================================
""")
    input("[Press Enter to continue.]")
    clearconsole()
    print("""
Pour connaître votre Classe, merci de fournir les données demandées ci-après.

CODE Spés :

 - NSI      = Numérique et Sciences de l'Informatique
 - HGGSP    = Histoire Géographie Géopolitique et Sciences Politiques
 - HLP      =
 - SI       = Sciences de l'Ingénieur
 - SES      = Sciences économiques et sociales
 - MATHS    = Mathématiques
 - LLCE_ENG = Anglais
 - LLCE_ESP = Espagnol
 - PC       = Physique Chimie
 - SVT      = Sciences de la Vie et de la Terre
 - ART_P    = Arts Plastiques
 - MUSIC    = Musique
 - THEATRE  = Théâtre

""")
    input("[Press Enter to continue.]")
    clearconsole()
    print("""
CODE Langues :

Etant donné qu'une erreur a probablement été effectuée lors des réglages des groupes de langues,
aucune différence sera faite entre LV1 et LV2.

 - ALL = Allemand
 - ESP = Espagnol
 - CHI = Chinois

""")
    input("[Press Enter to continue.]")
    clearconsole()
    print("""
CODE Options (Faculatif/Non implémenté) :
 - MATHSEXPERT
 - MATHSCOMP
 - DGEMC
 - EUROENG
 - EUROALL
 - ART_P
 - MUSIC
 - THEATRE
 - CHI3
 - LATIN
 - GREC
 
Merci d'indiquer ces codes pour chaque question
""")
    input("Press Enter to continue.")
    return None


# Bug
def loadcsv(file: str) -> list:
    with open(file, "r", encoding="utf-8") as fichier:
        rawdata = csv.reader(fichier, delimiter=';')
        output = []
        for i in rawdata:
            # print(i)
            output.append(i)
    fichier.close()
    return output


# Fini (pour l'instant)
def getinfo() -> tuple:
    spe1 = input("Spécialité 1 : ").upper()
    spe2 = input("Spécialité 2 : ").upper()
    lang = input("Langue Additionnelle : ").upper()
    return spe1, spe2, lang


# Fini/Non testé
def findclass(classe: list, spe1: str, spe2: str, lang: str) -> int:
    found = False
    for i in range(len(classe)):
        classe[i] = classe[i]
        print(classe[i])
        if spe1 in classe[i] and spe2 in classe[i] and lang in classe[i]:
            classeeleve = i
            found = True
            return classeeleve
    if not found:
        exit("findclass : Fetching Failed ! Please make sure you gave the right answers")


# Fini/Non testé
def fetchclassletter(classeeleve: int) -> str:
    listletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    lettreclasse = listletters[classeeleve]
    return lettreclasse.upper()


def newprint(speech: int):
    content = loadcsv("speech.csv")
    '''
    # dev only :
    content = ["=====================================================================================================================\n=====================================================================================================================\n===       ___           ___           ___           ___           ___           ___       ___           ___       ===\n===      /\  \         /\__\         /\  \         /\  \         /\  \         /\__\     /\  \         /\  \      ===\n===     /::\  \       /:/  /         \:\  \       /::\  \       /::\  \       /:/  /    /::\  \       /::\  \     ===\n===    /:/\:\  \     /:/  /           \:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \     /:/\ \  \    ===\n===   /::\~\:\  \   /:/  /  ___       /::\  \   /:/  \:\  \   /:/  \:\  \   /:/  /    /::\~\:\  \   _\:\~\ \  \   ===\n===  /:/\:\ \:\__\ /:/__/  /\__\     /:/\:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__\  ===\n===  \/__\:\/:/  / \:\  \ /:/  /    /:/  \/__/ \:\  \ /:/  / \:\  \  \/__/ \:\  \    \/__\:\/:/  / \:\ \:\ \/__/  ===\n===       \::/  /   \:\  /:/  /    /:/  /       \:\  /:/  /   \:\  \        \:\  \        \::/  /   \:\ \:\__\    ===\n===       /:/  /     \:\/:/  /     \/__/         \:\/:/  /     \:\  \        \:\  \       /:/  /     \:\/:/  /    ===\n===      /:/  /       \::/  /                     \::/  /       \:\__\        \:\__\     /:/  /       \::/  /     ===\n===      \/__/         \/__/                       \/__/         \/__/         \/__/     \/__/         \/__/      ===\n===                                                                                                               ===\n===                                              CLASSROOM RESOLVER                                               ===\n=====================================================================================================================\n=====================================================================================================================",
               "CODE Spés :\n\n - NSI      = Numérique et Sciences de l'Informatique\n - HGGSP    = Histoire Géographie Géopolitique et Sciences Politiques\n - HLP      =\n - SI       = Sciences de l'Ingénieur\n - SES      = Sciences économiques et sociales\n - MATHS    = Mathématiques\n - LLCE_ENG = Anglais\n - LLCE_ESP = Espagnol\n - PC       = Physique Chimie\n - SVT      = Sciences de la Vie et de la Terre\n - ART_P    = Arts Plastiques\n - MUSIC    = Musique\n - THEATRE  = Théâtre",
               "CODE Langues :\nEtant donné qu'une erreur a probablement été effectuée lors des réglages des groupes de langues,\naucune différence sera faite entre LV1 et LV2.\n\n - ALL = Allemand\n - ESP = Espagnol\n - CHI = Chinois",
               "CODE Options (Faculatif/Non implémenté) :\n - MATHSEXPERT\n - MATHSCOMP\n - DGEMC\n - EUROENG\n - EUROALL\n - ART_P\n - MUSIC\n - THEATRE\n - CHI3\n - LATIN\n - GREC"]
    '''
    if speech <= 1:
        clearconsole()
        toprint = content[speech][0].strip()
        print(toprint.replace('\\n', '\n'))
    else:
        clearconsole()
        print("Merci de répondre avec le code correspondant")
        print(content[speech][0])
    return None


"""DEBUG Zone
newprint(1)
# printinfo()
CLASSE = loadcsv("classevertical.csv")
INFO = getinfo()
CLASSEELEVE = findclass(CLASSE, INFO[0], INFO[1], INFO[2])
print(CLASSEELEVE)
print(fetchclassletter(CLASSEELEVE))
# print(CLASSE[0])
# print(loadcsv("classevertical.csv"))
# print(CLASSE)
"""

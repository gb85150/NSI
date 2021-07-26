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


# Pas fini
def loadcsv(file="classes.csv"):
    with open(file, "r") as fichier:
        rawdata = csv.reader(fichier)
        classe = 0
        for x in rawdata:
            classe.append(x)
    return classe


# Fini (pour l'instant)
def getinfo():
    SPE1 = input("Spécialité 1 : ")
    SPE2 = input("Spécialité 2 : ")
    LANG = input("Langue Additionnelle : ")
    SPE1.upper()
    SPE2.upper()
    LANG.upper()
    return SPE1, SPE2, LANG


def findclass(classe, spe1, spe2, lang, classeeleve=None):
    for i in classe:
        if spe1 in classe[i] and spe2 in classe[i] and lang in classe[i]:
            classeeleve = i
            return classeeleve
        else:
            print("Fetching Failed ! Please make sure you gave the right answers")
            break


def fetchclassletter(classeeleve):
    listletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    lettreclasse = listletters[classeeleve]
    return lettreclasse


printinfo()
loadcsv()
getinfo()
findclass(classe, SPE1, SPE2, LANG)
print(fetchclassletter())


# print(SPE1)
# print(SPE2)
# print(LANG)

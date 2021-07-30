# All rights are reserved by gb85 for this script
# THIS SOFT IS DISTRIBUTED WITHOUT ANY WARRANTY
import os
import platform
import csv
import time


def clearconsole() -> None:
    """
    FR :
    Fonction Basique permettant l'effacement de la console,
    Compatible Windows/DOS, Linux, MacOS
    Elle émule l'envoi d'une commande d'effacement dans le terminal.

    EN :
    Basic function allowing the erasing of the console,
    Compatible with Windows/DOS, Linux, MacOS
    It emulates the sending of a delete command in the terminal.
    """
    command = 'clear'
    if platform.system() == 'Windows':  # If Machine is running on Windows, use cls
        command = 'cls'
    elif 'Linux' == platform.system() or 'Darwin' == platform.system() or 'Java' == platform.system():
        command = 'clear'
    os.system(command)
    return None


def fetchclassletter(classeeleve) -> str:
    """
    FR :
    Fonction permettant de retrouver la lettre correspondante à son index.

    EN :
    Function to find the letter corresponding to its index.
    """
    listletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    lettreclasse = listletters[classeeleve]
    return lettreclasse.upper()


def newprint(speech: int) -> None:
    """
    FR :
    Méthode d'affichage moderne développée par mes soins pour permettre un Affichage simple des informations.

    EN :
    Modern display method developed by me to allow a simple display of information.
    """
    content = [
        "=====================================================================================================================\n=====================================================================================================================\n===       ___           ___           ___           ___           ___           ___       ___           ___       ===\n===      /\  \         /\__\         /\  \         /\  \         /\  \         /\__\     /\  \         /\  \      ===\n===     /::\  \       /:/  /         \:\  \       /::\  \       /::\  \       /:/  /    /::\  \       /::\  \     ===\n===    /:/\:\  \     /:/  /           \:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \     /:/\ \  \    ===\n===   /::\~\:\  \   /:/  /  ___       /::\  \   /:/  \:\  \   /:/  \:\  \   /:/  /    /::\~\:\  \   _\:\~\ \  \   ===\n===  /:/\:\ \:\__\ /:/__/  /\__\     /:/\:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__\  ===\n===  \/__\:\/:/  / \:\  \ /:/  /    /:/  \/__/ \:\  \ /:/  / \:\  \  \/__/ \:\  \    \/__\:\/:/  / \:\ \:\ \/__/  ===\n===       \::/  /   \:\  /:/  /    /:/  /       \:\  /:/  /   \:\  \        \:\  \        \::/  /   \:\ \:\__\    ===\n===       /:/  /     \:\/:/  /     \/__/         \:\/:/  /     \:\  \        \:\  \       /:/  /     \:\/:/  /    ===\n===      /:/  /       \::/  /                     \::/  /       \:\__\        \:\__\     /:/  /       \::/  /     ===\n===      \/__/         \/__/                       \/__/         \/__/         \/__/     \/__/         \/__/      ===\n===                                                                                                               ===\n===                                              CLASSROOM RESOLVER                                               ===\n=====================================================================================================================\n=====================================================================================================================",
        "CODE Spés :\n\n - NSI      = Numérique et Sciences de l'Informatique\n - HGGSP    = Histoire Géographie Géopolitique et Sciences Politiques\n - HLP      =\n - SI       = Sciences de l'Ingénieur\n - SES      = Sciences économiques et sociales\n - MATHS    = Mathématiques\n - LLCE_ENG = Anglais\n - LLCE_ESP = Espagnol\n - PC       = Physique Chimie\n - SVT      = Sciences de la Vie et de la Terre\n - ART_P    = Arts Plastiques\n - MUSIC    = Musique\n - THEATRE  = Théâtre",
        "CODE Langues :\nEtant donné qu'une erreur a probablement été effectuée lors des réglages des groupes de langues,\naucune différence sera faite entre LV1 et LV2.\n\n - ALL = Allemand\n - ESP = Espagnol\n - CHI = Chinois",
        "CODE Options (Faculatif/Non implémenté) :\n - MATHSEXPERT\n - MATHSCOMP\n - DGEMC\n - EUROENG\n - EUROALL\n - ART_P\n - MUSIC\n - THEATRE\n - CHI3\n - LATIN\n - GREC"
    ]
    if speech < 1:
        clearconsole()
        print(content[speech])
    else:
        clearconsole()
        print("Merci de répondre avec le code correspondant")
        print(content[speech])
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
    """
    FR :
    Fonction de récupération des informations de l'élève,
    elle appelle également newprint() pour l'affichage des informations.

    EN :
    Function to retrieve the student's information,
    it also calls newprint() to display the information.
    """
    newprint(0)
    wait()
    newprint(1)
    spe1 = input("Spécialité 1 : ").upper()
    newprint(1)
    spe2 = input("Spécialité 2 : ").upper()
    newprint(2)
    lang = input("Langue Additionnelle : ").upper()
    return spe1, spe2, lang


def wait() -> None:
    """
    FR :
    Fonction permettant de placer un délai matérialisé par une barre de progression.

    EN :
    Function allowing to place a delay materialized by a progress bar.
    """
    progress = [
        "[                                                  ] 0%",
        "[==========                                        ] 20%",
        "[====================                              ] 40%",
        "[==============================                    ] 60%",
        "[========================================          ] 80%",
        "[==================================================] 100%",
    ]
    print("Please wait...")
    print(progress[0])
    time.sleep(5)
    clearconsole()
    for i in range(1, 6):
        time.sleep(2)
        clearconsole()
        print(progress[i])
    return None


def findclass(spe1: str, spe2: str, lang: str) -> int:
    """
    FR :
    Le coeur du programme :
    Il permet de retrouver la classe de l'élève en comparant les données fournies avec celles de la base de données.

    EN :
    Core of the program:
    It finds the student's class by comparing the data provided with the data in the database.
    """
    found = False
    for i in range(len(classe)):
        classe[i] = classe[i]
        print(classe[i])
        if spe1 in classe[i] and spe2 in classe[i] and lang in classe[i]:
            classeeleve = i
            found = True
            return classeeleve
    exit("findclass : Fetching Failed ! Please make sure you gave the right answers \n findclass : Echec de la recherche ! Veuillez vous assurer que vous avez donné les bonnes réponses")


# Functions Calls
INFO = getinfo()
CLASSEELEVE = findclass(INFO[0], INFO[1], INFO[2])
print(f"Ta classe est la Terminale {fetchclassletter(CLASSEELEVE)} !")
print(f"Your class is the Terminale {fetchclassletter(CLASSEELEVE)} !")

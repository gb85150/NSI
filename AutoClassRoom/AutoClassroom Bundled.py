import os
import platform
import time


def clearconsole():
    command = 'clear'
    if platform.system() == 'Windows':  # If Machine is running on Windows, use cls
        command = 'cls'
    elif 'Linux' == platform.system() or 'Darwin' == platform.system() or 'Java' == platform.system():
        command = 'clear'
    os.system(command)
    return None


def fetchclassletter(classeeleve):
    listletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    lettreclasse = listletters[classeeleve]
    return lettreclasse.upper()


def newprint(speech: int):
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


def getinfo() -> tuple:
    newprint(0)
    wait()
    newprint(1)
    spe1 = input("Spécialité 1 : ").upper()
    newprint(2)
    spe2 = input("Spécialité 2 : ").upper()
    newprint(3)
    lang = input("Langue Additionnelle : ").upper()
    return spe1, spe2, lang


def wait() -> None:
    progress = [
        "[                                                  ] 0%",
        "[==========                                        ] 10%",
        "[====================                              ] 20%",
        "[==============================                    ] 30%",
        "[========================================          ] 40%",
        "[==================================================] 50%",
    ]
    print("Please wait...")
    print(progress[0])
    for i in range(1, 6):
        time.sleep(1)
        clearconsole()
        print(progress[i])
    return None


def findclass(spe1: str, spe2: str, lang: str) -> int:
    found = False
    classe = [
        ["ESP", "ALL", "HLP", "LLCE_ENG", "MATHS", "NSI", "PC", "SVT", "SES", "HGGSP", "THEATRE", "ART_Pop", "CHI3", "MUSICop", "THEATREop", "ART_Pop", "EUROENG", None, None, None],
        ["ESP", "HGGSP", "HLP", "LLCE_ENG", "SVT", "SES", "MUSIC", "THEATRE", "ART_P", "CHI3", "MUSICop", "THEATREop", "EUROENG", None, None, None, None, None, None, None],
        ["ALL", "ESP", "HGGSP", "HLP", "NSI", "PC", "SVT", "SES", "MUSIC", "THEATRE", "ART_P", "DGEMC", "MATHSCOMP", "GREC", "CHI3", "MUSICop", "THEATREop", "ART_Pop", "EUROENG", None],
        ["ALL", "ESP", "HGGSP", "LLCE_ENG", "MATHS", "PC", "SVT", "SES", "THEATRE", "ART_P", "DGEMC", "MATHSCOMP", "GREC", "CHI3", "MUSICop", "THEATREop", "ART_Pop", "EUROENG", None, None],
        ["ALL", "ESP", "HGGSP", "HLP", "LLCE_ENG", "MATHS", "NSI", "PC", "SVT", "SES", "THEATRE", "ART_P", "DGEMC", "MATHSCOMP", "MATHSEXPERT", "LATIN", "MUSICop", "THEATREop", "ART_Pop", "EUROENG"],
        ["ALL", "ESP", "HGGSP", "HLP", "LLCE_ENG", "MATHS", "PC", "SVT", "SES", "MUSIC", "THEATRE", "DGEMC", "MATHSCOMP", "MATHSEXPERT", "LATIN", "GREC", "CHI3", "ART_Pop", "EUROENG", "EUROALL"],
        ["ALL", "ESP", "HGGSP", "HLP", "LLCE_ENG", "LLCE_ESP", "MATHS", "PC", "SVT", "SES", "MUSIC", "THEATRE", "DGEMC", "MATHSCOMP", "LATIN", "GREC", "CHI3", "MUSICop", "ART_Pop", "EUROENG"],
        ["ALL", "ESP", "CHI", "MATHS", "NSI", "PC", "SVT", "SES", "MUSIC", "THEATRE", "ART_P", "DGEMC", "MATHSCOMP", "LATIN", "MUSICop", "THEATREop", "ART_Pop", "EUROENG", None, None],
        ["ALL", "ESP", "CHI", "MATHS", "NSI", "PC", "SVT", "SI", "DGEMC", "MATHSCOMP", "MATHSEXPERT", "GREC", "CHI3", "ART_Pop", "EUROENG", None, None, None, None, None],
        ["ALL", "ESP", "CHI", "HGGSP", "HLP", "LLCE_ENG", "MATHS", "SES", "THEATRE", "ART_P", "DGEMC", "MATHSCOMP", "LATIN", "CHI3", "MUSIQUE", "THEATRE", "EUROENG", "EUROALL", None, None]
    ]
    for i in range(len(classe)):
        classe[i] = classe[i]
        print(classe[i])
        if spe1 in classe[i] and spe2 in classe[i] and lang in classe[i]:
            classeeleve = i
            return classeeleve
    exit("findclass : Fetching Failed ! Please make sure you gave the right answers")


INFO = getinfo()
CLASSEELEVE = findclass(INFO[0], INFO[1], INFO[2])
print(fetchclassletter(CLASSEELEVE))

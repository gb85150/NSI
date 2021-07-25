import os
import platform


def clearconsole():
    command = 'clear'
    if platform.system() == 'Windows':  # If Machine is running on Windows, use cls
        command = 'cls'
    elif 'Linux' == platform.system() or 'Darwin' == platform.system() or 'Java' == platform.system():
        command = 'clear'
    os.system(command)


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
===                                                 Classroom resolver                                            ===                                                                                     ===
=====================================================================================================================
=====================================================================================================================
""")
input("[Press Enter to continue.]")
clearconsole()
print("""
Pour connaître votre Classe, merci de fournir les données demandées ci-après.

CODE Spés :

 - NSI     = Numérique et Sciences de l'Informatique
 - HGGSP   = Histoire Géographie Géopolitique et Sciences Politiques
 - HLP     =
 - SI      = Sciences de l'Ingénieur
 - SES     = Sciences économiques et sociales
 - MATHS   = Mathématiques
 - LLCE    = Anglais
 - PC      = Physique Chimie
 - SVT     = Sciences de la Vie et de la Terre
 - AR_P    = Arts Plastiques
 - MUSIC   = Musique
 - THEATRE = Théâtre

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
 - EPS
 - EUROENG
 - EUROALL
 - ARTP
 - MUSIC
 - THEATRE
 - CHINOIS
 - LATIN
 - GREC
 
Merci d'indiquer ces codes pour chaque question
""")
input("Press Enter to continue.")
SPE1 = input("Spécialité 1 :")
SPE2 = input("Spécialité 2 :")
LANG = input("Langue Additionnelle :")
SPE1.upper()
SPE2.upper()
LANG.upper()
print(SPE1)
print(SPE2)
print(LANG)

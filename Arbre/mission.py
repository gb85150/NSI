from arbre_binaire_jeu import *

#-------------------------------------------------------------------------------
#                           DM MISSION
#
# Objectif : Construire un jeu à partir d'un texte préconstruit
#
# Contrainte : utiliser un arbre binaire
#-------------------------------------------------------------------------------

# Phrases préconstruites

phrases = [None] * 18
phrases[0] = """21/10/2024 - 03h30, New York, un quartier mal famé et mal éclairé. Vous êtes au pied de l'immeuble auquel vous a mené votre enquête.
25 étages à vue de nez. Même au coeur de la nuit,  on voit qu'il aurait besoin au minimum d'un sacré coup de peinture ; on le donnerait pour
abandonné si on ne percevait pas ça et là de faibles rayons de lumière. Tout est calme alentour, un silence à couper au couteau.
D'après mon informateur, le fils du Président, retenu prisonnier par le Gang des Ignares, est situé tout en haut au dernier étage.
Il est probablement sous surveillance. Pour le libérer, il va falloir être discret..."""
phrases[1] = "Damnation, je ne peux plus avancer! Il va falloir tenter la voie des airs, ça va être compliqué ..."
phrases[2] = "La porte d'entrée n'offre pas de résistance, je traverse le hall vers les accès aux étages."
phrases[3] = "Quelle malchance, l'ascenseur n' a plus d 'électricité. je vois un boîtier avec des fils qui dépassent."
phrases[4] = "L'escalier est fermé par une énorme grille. Il y a un boîtier avec un code à taper."
phrases[5] = "Ca y est, l'ascenseur fonctionne. Voilà, je suis dedans et je monte."
phrases[6] = "Ca y est, la grille s'ouvre. Prenons l' escalier. A moi les 25 étages...pfff !"
phrases[7] = """Ascension terminée, me voici à pied d'oeuvre! Je découvre un couloir. Il y a une porte latérale ouverte, ce doit être celle du gardien.
La porte fermée au fond doit être celle du prisonnier"""
phrases[8] = "Sacrebleu ! J 'ai foutu en l'air cette boîte rouillée qui s'est appelée un jour ascenseur. Voyons l'escalier..."
phrases[9] = "Enfer, le code ne marche pas, la grille est bloquée l'escalier est inaccessible. Voyons l'ascenseur..."
phrases[10] = "C'est la catastrophe, je ne peux pas monter, j' abandonne la mission en attendant de trouver un autre moyen"
phrases[11] = "Malédiction, le couloir est allumé, je vais me faire repérer, à moins qu' il dorme"
phrases[12] = "Le couloir est dans l'obscurité, pas de lumière, je vais me glisser dans l'ombre, il ne me verra pas"
phrases[13] = "Pas de bruit sauf une légère respiration, le surveillant doit dormir, je tente ma chance"
phrases[14] = "Des bruits de table et de chaise, le surveillant est apparemment bien éveillé."
phrases[15] = """Ouf, j'ai pu passer le couloir sans encombre. J'ouvre la porte au fond. Le prisonnier tourne la tête lentement
vers moi et me lance un regard ébahi. Je prend la pose et je lui lance un « Salut fiston, ton sauveur est arrivé! »"""
phrases[16] = """Un jet de lumière, le gardien braque sur moi un gros flingue, un sourire mauvais éclaire son visage ;
manifestement il m'attendait c'est un piège !"""
phrases[17] = "C'est trop risqué pour l' instant, je reviendrai dans quelques heures."

questions = [None] * 6
questions[0] = "La porte de l'immeuble est-elle ouverte (taper 1) ou verrouillée (taper 0) ? "
questions[1] = "Choisissez vous de prendre l'ascenseur (taper 1) ou l'escalier (taper 0)? "
questions[2] = "Branchez vous le fil vert avec noir (taper 1) ou le rouge avec le noir (taper 0)? "
questions[3] = "Choisissez vous le code 1111 (taper 1) ou le code 9999 (taper 0)? "
questions[4] = "Le couloir en face est-il éclairé (taper 1) ou dans le noir (taper 0)? "
questions[5] = "Entendez vous quelqu'un qui s'agite dans la pièce de surveillance (taper 1) ou est elle silencieuse (taper 0) ? "

# déroulement de l'histoire (aide)
'''
porte ouverte ou fermée ?
porte ouverte, choix ascenseur ou escalier
porte fermée, fin de l' histoire
ascenseur, fil vert ou rouge
ascenseur marche, arrivée en haut, question sur lumière couloir
ascenseur en panne, test escalier
couloir allumé, bruit ?
trop risqué
sauvé
couloir éteint, bruit ?
sauvé
piège
escalier, 1111 ou 9999 ?
escalier marche, arrivée en haut, question sur lumière couloir ...
escalier foutu, test ascenseur
escalier bloqué, mission reportée
'''
arbre_jeu = Noeud((phrases[0] + questions[0]), 
                   Noeud(phrases[1],
                         None, 
                         None
                        ),
                   Noeud((phrases[2] + questions[1]),
                         Noeud((phrases[3] + questions[2]),
                                Noeud((phrases[8] + phrases[4] + questions[3]),
                                       "Fin Bis", 
                                       None
                                     ),
                                Noeud((phrases[6] + phrases[7] + questions[4])
                                     Noeud((phrases[11] + questions[5]),
                                            Noeud((phrases[13] + phrases[16]),   # Fin
                                                 None,
                                                 None
                                                 )
                                          ),
                                     Noeud((phrases[12] + phrases[15]))
                                     )
                              ),
                         Noeud((phrases[4] + phrases[3]),
                         Noeud,
                         Noeud((phrases[6] + phrases[7] + questions[4])
                                     Noeud((phrases[11] + questions[5]),
                                            Noeud((phrases[13] + phrases[16]),   # Fin
                                                 None,
                                                 None
                                                 )
                                          ),
                                     Noeud((phrases[12] + phrases[15]))
                                     )
                         ),
                        )
                 )
print("....!! FIN !!...")


#-------------------------------------------------------------------------------
#                                 QUESTIONS
#
# 1. a) Sur papier, construire l'arbre en notant comme étiquette de noeud les phrases et la question éventuelle associées
#    b) Déterminer la taille et la hauteur de l'arbre. Combien comporte-t-il de feuilles ?
# 2. A l'aide du module arbre_binaire importé, constuire l'arbre précédent en python.
# 3. Ecrire une fonction qui parcours l'arbre comme dans en affichant le texte dans la console et les questions
#    sous forme d'input pour lequel le joueur répond 0 ou 1.
# 4. Tester le jeu.

# blackjack
from random import randint
nbredes = int(input("combien désirez-vous lancer de dés ? "))
for k in range(nbredes):
    resultatjoueur = 0
    resultatjoueur = resultatjoueur + randint(1, 6)
for k in range(nbredes):
    resultatbanque = 0
    resultatbanque = resultatjoueur + randint(1, 6)
# vérification égalité
if resultatjoueur > 21 and resultatbanque > 21:
    print("égalité !")
elif resultatjoueur > 21:
    print("banque gagnante !")
elif resultatbanque > 21:
    print("joueur gagnant !")
elif resultatjoueur > resultatbanque:
    print("joueur gagnant !")
elif resultatbanque > resultatjoueur:
    print("banque gagnante !")
else:
    print("une erreur s'est produite veuillez nous excuser pour la gêne occasionnée cordialement, le service de débugging")

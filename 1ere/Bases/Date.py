# Calculateur de JOURS --EXPERIMENTAL--
# Geoffrey BOUSSEAU 1F
# ce programme calcule en jours l'écart entre deux dates donnés
# this script is calculating the number of days beetween 2 dates given before


andépart = int(input("l'année de départ "))
moisdépart = int(input("le mois de départ au format 0X ou XX "))
jourdépart = int(input("le jour de départ "))
anarrivée = int(input("l'année d'arrivée "))
moisarrivée = int(input("le mois d'arrivée au format 0X ou XX "))
joursarrivée = int(input("le jour d'arrivée "))
# vérification année bissextile


def bissextile(an):
    return(an % 4) == 0 and not (an % 100) == 0 or (an % 400) == 0


# calcul nb de jours pour 1an
def nbjoursannee(an):
    if bissextile(an):
        nban = 366
    else:
        nban = 365
    return(nban)
    print(nban)
# nbjour pour 1mois


def nbjoursmois(an, mois):
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        nbmois = 31
    elif mois == 2:
        if bissextile(an):
            nbmois = 29
        else:
            nbmois = 28
    else:
        nbmois = 30
    return(nbmois)
    print(nbmois)


# Calcul du nbre de jours total
def nbjours(jourdépart, moisdépart, andépart, jours, mois, an):
    jours = 0
    # Les années
    for i in range(andépart + 1, an):
        jours = jours + nbjoursannee(i)
        return(jours)
    # Les mois
    for i in range(moisdépart + 1, mois):
        jours = jours + nbjoursmois(i)
        return(jours)
    # Les jours
    jours


print(nbjours(jourdépart, moisdépart, andépart, joursarrivée, moisarrivée, anarrivée))

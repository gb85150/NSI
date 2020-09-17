an = int(input("l'année"))
mois = int(input("le mois au format 0X ou XX"))
jour = int(input("le jour"))
# vérification année bissextile


def bissextile(an):
    return(an % 4) == 0 and not (an % 100) == 0 or (an % 400) == 0


# calcul nb de jours pour 1an
def nbjoursannee(an):
    if bissextile(an) :
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
        if isbissextile(an):
            nbmois = 29
        else:
            nbmois = 28
    else:
        nbmois = 30
    return(nbmois)
    print(nbmois)
    

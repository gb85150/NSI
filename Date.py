an = int(input("l'année"))
mois = int(input("le mois au format 0X ou XX"))
# vérification année bissextile
def bissextile(an):
    if (an % 4) == 0 or (an % 400) == 0:
        isbissextile = True
        if (an % 100) == 0:
            isbissextile = False
        else:
            isbissextile = False
    else:
        isbissextile = False
    return(isbissextile)
# print(bissextile(an))
# calcul nb de jours pour 1an
def nbjoursannee(isbissextile):
    nban = 0
    if isbissextile == True:
        nban = 366
    else:
        nban = 365
    return(nban)
print(nban)
# nbjour pour 1mois
def nbjoursmois(isbissextile, mois):
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        nbmois = 31
    elif mois == 2:
        if isbissextile == True:
            nbmois = 29
        else:
            nbmois = 28
    else:
        nbmois = 30
    return(nbmois)
print(nbmois)

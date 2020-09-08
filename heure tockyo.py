heure_locale = int("saisir l'heure sans les minutes :")
heure_tokyo = heure_locale + 7
if heure_tokyo < 24 :
    heure_tokyo = heure_tokyo - 24
print("si il est ",heure_locale,"heures, alors il est ",heure_tokyo,"heures à tokyo.")
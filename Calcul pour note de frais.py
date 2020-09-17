D = int(input("Saisir le nombre de kilomètres parcourus : "))
if D <= 5000:
    F = D*0.536
else:
    if D <= 20000:
        F = 1180+D*0.30
    else:
        F = D*0.359
print("Vos frais kilométriques s'élèvent à ", F, "Euros HT")

money_request = int(input("saisir le montant demandé : "))
# division euclidienne "doublée" afin de récupérer le reste ainsi que le nombre de billet
billet_number200 = money_request//200
billet_reste = money_request % 200
billet_number100 = billet_reste//100
billet_reste = billet_reste % 100
billet_number50 = billet_reste//50
billet_reste = billet_reste % 50
billet_number20 = billet_reste//20
billet_reste = billet_reste % 20
billet_number10 = billet_reste//10
# Affichage de la composition des billets en vue de l'appel d'une fonction
print("nombre de billet de 200 : ", billet_number200)
print("nombre de billet de 100 : ", billet_number100)
print("nombre de billet de 50 : ", billet_number50)
print("nombre de billet de 20 : ", billet_number20)
print("nombre de billet de 10 : ", billet_number10)

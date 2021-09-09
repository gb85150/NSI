import csv

with open("rando.csv", "r") as fichier:
    table = csv.reader(fichier)
    t = []
    entete = []
    for ligne in table:
        t.append(tuple(ligne[0], ligne[1]))
        entete.append(table[0])
        t.remove(0)


alt, dis = [], []
entete = []
for ligne in t:
    a, b = ligne()
    alt.append[a]
    dis.append[b]
entete.append(tuple(table[0]))


print(alt, dis)

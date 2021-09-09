# custom count
def count(valeur, tableau):
    countresult = 0
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            countresult += 1
    return countresult

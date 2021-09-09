liste = [4, 9, 6, 7, 12, 3, 4]


def tri_insertion(liste):
    for i in range(1, len(liste)):
        elt = liste[i]
        j = i - 1
        while j >= 0 and liste[j]:
            liste[j + 1] = liste[j]
            j = j - 1
        liste[j + 1] = elt
    return liste


list(liste)
tri_insertion(liste)
def total_hors_reduction(tab:list) -> float:
    return sum(tab)

def total_reduction(tab:list) -> int:
    return sum(total_hors_reduction(tab) * 1-0.1*len(tab))

def minimum(tab:list) -> int:
    return min(tab)

def offre_bon_clients(tab:list) -> int:
    if len(tab) >= 2: return sum(tab) - minimum(tab)
    else: return sum(tab)

def destockage(tab:list) -> int:
    for i in range(len(tab)):
        if (i + 3) < len(tab):
            item = []
            for j in range(3):
                item.append(tab[i+j])
            tab.remove(tab[minimum(item)+i])
    return sum(tab)

if __name__ == "__main__":
    tab = [30.5, 15.0, 6.0, 20.0, 5.0, 35.0, 10.5]
    print(total_hors_reduction(tab))
    print(total_reduction(tab))
    print(minimum(tab))
    print(offre_bon_clients(tab))
    print(destockage(tab))
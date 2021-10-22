class Pile:
    def __init__(self):
        self.pile = []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        out = self.pile.pop()
        return out


class File:
    def __init__(self):
        self.liste = []

    def lister(self, element):
        self.liste.append(element)

    def delister(self):
        self.liste.remove(0)


TABLE = Pile
LISTE = File
TABLE.empiler(5)
print(TABLE.depiler())
print("================================")
for i in range(999):
    LISTE.lister(i)
print(LISTE)
LISTE.delister()
print(LISTE)

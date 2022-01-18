class Noeud :
        def __init__(self, cle):
             self.cle = cle
             self.gauche = None
             self.droit = None

        def insere(self, cle):
             if cle < self.cle :
                if self.gauche == None :
                     self.gauche = Noeud(cle)
                else :
                     self.gauche.insere(cle)
            elif cle > self.cle :
                 if self.droit == None :
                    self.droit = Noeud(cle)
                 else :
                    self.droit.insere(cle)

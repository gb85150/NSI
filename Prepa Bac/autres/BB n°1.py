class Noeud:
	def __init__(self, cle):
		self.cle = cle
		self.gauche = None
		self.droit = None

	def insere(self, cle):
		if cle < self.cle :
			if self.gauche == None:
				self.gauche = Noeud(cle)
			else :
				self.gauche.insere(cle)
		elif cle > self.cle :
			if self.droit == None:
				self.droit = Noeud(cle)
			else:
				self.droit.insere(cle)
	def hauteur(self):
		if self.gauche == None and self.droit == None:
			return 0
		if self.gauche == None:
			return 1 + self.droit.hauteur()
		elif self.droit == None:
			return 1 + self.gauche.hauteur()
		else:
			hg = self.gauche.hauteur()
			hd = self.droit.hauteur()
			if hg > hd:
				return hg+1
			else:
				return hd+1


class Arbre:
	def __init__(self, cle):
		self.racine = Noeud(cle)

	def insere(self, cle):
		self.racine.insere(cle)

	def hauteur(self):
		return self.racine.hauteur()
	

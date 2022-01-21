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
	
	def taille(self):
		if self.gauche == None and self.droit == None:
			return 1
		if self.gauche == None:
			return 1 + self.droit.taille()
		elif self.droit == None:
			return 1 + self.gauche.taille()
		else:
			return 1 + self.gauche.taille() + self.droit.taille()


class Arbre:
	def __init__(self, cle):
		self.racine = Noeud(cle)

	def insere(self, cle):
		self.racine.insere(cle)

	def hauteur(self):
		return self.racine.hauteur()
	
	def taille(self):
		return self.racine.taille()
	
	def bien_construit(self):
		"""
			Vérifie si l'arbre binaire de recherche est bien compris entre (2**(h+1m))-1 et 2**h
		"""
		return self.taille() == (2**self.hauteur()+1)-1 or self.taille == 2**self.hauteur()
	

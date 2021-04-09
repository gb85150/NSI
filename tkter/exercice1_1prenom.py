import tkinter as tk
# FONCTIONS


def afficher(event):
    """
    Fonction qui transforme le texte dans champ_label2
    @faux parametre : "event" n'est pas un paramètre passé en
    argument,il désigne juste l'événement qui se produit lorsque l'on appuie
    sur la touche entrée
    @faux return : la chaîne de caractères stockée dans champ_label2
    est modifiée avec le texte récupéré par la méthode "texte.get()", il n'y
    a pas de retour
    """
    champ_label2.configure(text="bonjour " + texte.get())
    return None


# PROGRAMME PRINCIPAL
fen1 = tk.Tk()
# On dimensionne la fenetre
fen1.geometry("400x100")
# On lui donne un titre
fen1.title("Ma fenêtre")
# On la colore
fen1.config(background="Yellow")
# On crée un label (ligne de texte) de titre
champ_label = tk.Label(fen1, text="Bienvenue dans ce nouveau monde !")
# On affiche le label dans la fenêtre, au milieu par défaut
champ_label.pack()
# On crée un deuxième label
champ_label2 = tk.Label(fen1, text="Entrez votre nom")
# On affiche le label dans la fenêtre, à gauche
champ_label2.pack(side="left")
# On crée puis un champ de saisie
# le champ de saisie donne une variable nommée texte
texte = tk.Entry(fen1, width=20)
# quand on appuie sur entrée, on appelle la fonction "afficher"
texte.bind("<Return>", afficher)
# On affiche le texte dans la fenêtre
texte.pack()
# on ajoute un bouton "quitter", avec une commande fen1.destroy au nom

bouton_quitter = tk.Button(fen1, text="Quitter", command=fen1.destroy)
# On affiche le bouton dans la fenêtre
bouton_quitter.pack()
# On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre
fen1.mainloop()

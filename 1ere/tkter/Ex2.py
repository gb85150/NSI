import tkinter as tk


# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
def evaluer(event):
    if entree.get() == "shut up!":
        fenetre.destroy()
    else:
        chaine.configure(text="Résultat = " + str(eval(entree.get())))


# ----- Programme principal : ----
fenetre = tk.Tk()
fenetre.protocol('WM_DELETE_WINDOW', fenetre.iconify)
fenetre.geometry("250x60")
entree = tk.Entry(fenetre)
entree.bind("<Return>", evaluer)
entree.pack(pady=10)
chaine = tk.Label(fenetre)
chaine.pack()
fenetre.mainloop()

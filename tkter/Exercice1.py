import tkinter as tk
from tkinter import messagebox


def askquit():
    if messagebox.askokcancel("Quit", "J'adore les popups"):
        fen1.destroy


fen1 = tk.Tk()
fen1.title("pranked")
fen1.config(bg="Red")
fen1.geometry("400x100")
Ok = tk.Button(fen1, text='Ok !', command=askquit())
text = tk.Label(fen1, fg='Red', text="""Bonjour tout le monde
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Mauris vel aliquet augue, ac accumsan augue. Nam eleifend,
enim et egestas posuere, nulla ipsum suscipit erat.
""")
text.pack()
Ok.pack()
fen1.protocol('WM_DELETE_WINDOW', fen1.iconify)
fen1.mainloop()

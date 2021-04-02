from tkinter import *


fen1 = Tk()
fen1.title("pranked")
fen1.config(bg="Red")
fen1.geometry("400x100")
Ok = Button(fen1, text='Ok !', command=fen1.destroy)
text = Label(fen1, fg='Red', text="""Bonjour tout le monde
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Mauris vel aliquet augue, ac accumsan augue. Nam eleifend,
enim et egestas posuere, nulla ipsum suscipit erat.
""")
text.pack()
Ok.pack()
fen1.mainloop()

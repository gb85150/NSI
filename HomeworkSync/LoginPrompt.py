from tkinter import Tk, Entry, Label, Button, PhotoImage, StringVar
from tkinter import ttk


def login() -> str:
    """
    Shows a window to the user asking him to put his ED credentials
    :return: str
    """
    global root
    root=Tk()
    root.tk.call("source", r"HomeworkSync/res/W11/sun-valley.tcl")
    root.tk.call("set_theme", "dark")
    root.title("Login")
    root.geometry("300x350")
    root.resizable(False, False)
    root.configure()

    #Variables de stockage des Entry
    emailVar=StringVar()
    passwordVar=StringVar()

    # Logo
    logo = PhotoImage(file=r"HomeworkSync/res/logoEcoleDirecte.png")
    logo.zoom(25)
    logo_label = Label(root, image=logo)
    logo_label.image = logo
    logo_label.pack(padx=10, pady=10)

    label_email = Label(root, text="Email")
    label_email.pack(padx=10, pady=10)

    entry_email = Entry(root, textvariable=emailVar, width=40)
    entry_email.pack(padx=5, pady=5)
    
    label_password = Label(root, text="Password")
    label_password.pack(padx=10, pady=10)
    
    entry_password = Entry(root, textvariable=passwordVar, show="*", width=40)
    entry_password.pack(padx=5, pady=5)
    
    button_login = Button(root, text="Login", command=root.destroy)
    button_login.pack(ipadx=10, ipady=10, padx=10, pady=10)
    
    root.mainloop()
    return emailVar.get(), passwordVar.get()

if __name__ == "__main__":
    print(login())

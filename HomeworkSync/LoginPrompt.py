from logging import PlaceHolder
from operator import length_hint
import tkinter as tk


def login() -> str:
    """
    Shows a window to the user asking him to put his ED credentials
    :return: str
    """
    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("200x350")
    root.resizable(False, False)
    root.configure(background="SteelBlue2", borderwidth=0, highlightthickness=0, relief="flat", padx=0, pady=0)

    # Logo
    logo = tk.PhotoImage(file="HomeworkSync/res/logoEcoleDirecte.png", format="png")
    logo.zoom(25)
    logo_label = tk.Label(root, image=logo, background="SteelBlue2")
    logo_label.image = logo
    logo_label.pack(padx=10, pady=10)

    label_email = tk.Label(root, text="Email")
    label_email.pack(padx=10, pady=10)

    entry_email = tk.Entry(root)
    entry_email.pack(padx=5, pady=5)
    
    label_password = tk.Label(root, text="Password")
    label_password.pack(padx=10, pady=10)
    
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(padx=5, pady=5)
    
    button_login = tk.Button(root, text="Login", command=root.destroy)
    button_login.pack(ipadx=10, ipady=10, padx=10, pady=10)
    
    root.mainloop()
    return entry_email.get() + " " + entry_password.get()


if __name__ == "__main__":
    print(login())
    root.destroy()
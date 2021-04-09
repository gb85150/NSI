import tkinter as tk


def init(title):
    """
    @copyright 2021 MIT Geoffrey BOUSSEAU
    Crée une fenêtre [main_window] en fonction d'un titre [title]
    :param title: le titre de la fênetre
    :return: None
    """
    global main_window
    main_window = tk.Tk()
    main_window.title(title)
    main_window.mainloop()
    return None


def add():
    """
    Ajoute 1 à une variable globale [count]
    :return: La variable count est incrémentée de 1
    """
    global count
    count += 1
    return None


click_button = tk.Button(main_window, text='+1', command=add())
click_button.pack()
show_count = tk.Label(main_window, text=count)
show_count.pack()
init("Mon super compteur")

import tkinter as tk


def add():
    """
    Ajoute 1 à une variable globale [count]
    :return: La variable count est incrémentée de 1
    """
    global count
    count += 1
    return count


count = -1
main_window = tk.Tk()
main_window.title("Mon super compteur")
main_window.geometry("200x200")
click_button = tk.Button(main_window, text='+1', command=add())
click_button.pack()
show_count = tk.Label(main_window, text=count)
show_count.pack()
main_window.mainloop()

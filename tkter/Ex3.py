import tkinter as tk
from random import randint


def chk_num(num):
    if button1.get() > num:
        plus_or_minus = "The number is bigger"
    elif button1.get() < num:
        plus_or_minus = "The number is + petit"
    return plus_or_minus


# init
num = randint(1, 1000)
plus_or_minus = str()
main_window = tk.Tk()
main_window.title("Numbers Guess")
main_window.geometry("1920x1080")
input_number = tk.Entry(main_window)
input_number.bind("<Return>", chk_num)
button1 = tk.Button(main_window, text="Guess !", command=chk_num(num))
instructions = tk.Label(main_window, text="Try to Guess the number")
hint = tk.Label(main_window, text=plus_or_minus)
# DEBUG:
bonus = tk.Label(main_window, text=num)
bonus.pack()

input_number.pack()
button1.pack()
main_window.mainloop()

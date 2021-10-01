# this is the file which contains the GUI and is therefore the one from where the program should be run
import constants as c
import helpers as h
import tkinter as tk
from tkinter import ttk
from time import sleep

def run():
    root = tk.Tk()
    root.title("MLAatKST")
    root.geometry("300x700+100+100")

    menuPosition = 0

    if menuPosition == 0:
        h.startScreen(window = root)
    
    elif menuPosition == 1:
        h.book(window = root)

    elif menuPosition == 2:
        h.bookScnd(window = root)

    elif menuPosition == 3:
        h.web(window = root)

    root.mainloop()

if __name__ == "__main__":
    run()
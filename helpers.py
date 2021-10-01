# this is the file for the helper functions

import constants as c
import tkinter as tk
from tkinter import ttk

def startScreen(window):
    window.title("MLAatKST")
    window.geometry("300x700+100+100")

    title = tk.Label(
        window,
        text="MLA-Standard an der KST",
        font=("Futura", 16)
    )

    title.pack()

def book(window):
    window.title("MLAatKST")
    window.geometry("300x700+100+100")

    title = tk.Label(
        window,
        text="Buch",
        font=("Futura", 16)
    )

    title.pack()

def bookScnd(window):
    nothing = {}

def web(window):
    nothing = {}
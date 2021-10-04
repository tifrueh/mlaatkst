import tkinter as tk
import constants as c
from tkinter import ttk
from BookFrame import BookFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLA @ KST")
        self.geometry("600x600+50+50")
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    app.mainloop()
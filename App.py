import CitationFormatter
import tkinter as tk
from tkinter import ttk
import constants as c

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLA @ KST")
        self.geometry("300x600+50+50")
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    app.mainloop()
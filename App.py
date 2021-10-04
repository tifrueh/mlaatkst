import tkinter as tk
import constants as c
from tkinter import ttk
from EntryFrame import EntryFrame
from ControlFrame import ControlFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(c.TITLE)
        self.geometry("700x700+50+50")
        self.resizable(False, False)

        self.columnconfigure(index=0, weight=1)

        self.titleLabel = ttk.Label(self, text=c.TITLE_LABEL, font=("Futura", 20))
        self.titleLabel.grid(column=0, row= 0, pady=10)

if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()
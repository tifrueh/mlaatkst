import tkinter as tk
import constants as c
from tkinter import ttk
from EntryFrame import EntryFrame
from ControlFrame import ControlFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLA @ KST")
        self.geometry("700x700+50+50")
        self.resizable(False, False)

        self.columnconfigure(index=0, weight=1)

        self.titleLabel = ttk.Label(self, text="MLA-Standard an der KST", font=("Futura", 16))
        self.titleLabel.grid(column=0, row= 0, pady=10)

if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()
import tkinter as tk
from tkinter.font import Font
import constants as c
from tkinter import ttk
from BookFrame import BookFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MLA @ KST")
        self.geometry("700x700+50+50")
        self.resizable(False, False)

        self.columnconfigure(index=0, weight=1)

        self.titleLabel = tk.Label(self, text="MLA-Standard an der KST", font=("Futura", 16))
        self.titleLabel.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
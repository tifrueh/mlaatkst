import os
import tkinter as tk
from tkinter import ttk

import constants as c
from control_frame import ControlFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.appPath = os.path.dirname(__file__)
        self.imagePath = os.path.join(self.appPath, "resources", "bg2.png")
        self.bg = tk.PhotoImage(file=self.imagePath, format="png")
        self.bgLabel = ttk.Label(self, image=self.bg)
        self.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.title(c.TITLE)
        self.geometry("700x700+50+50")
        self.resizable(False, False)

        self.columnconfigure(index=0, weight=1)

        self.titleLabel = ttk.Label(self, text=c.TITLE_LABEL, font=("Futura", 20))
        self.titleLabel.grid(column=0, row=0, pady=40)


if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()

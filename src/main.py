#   MLA at KST: Citation helper for KST students
#   Copyright (C) 2021 Timo Früh
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import tkinter as tk
from tkinter import ttk

import constants as c
from control_frame import ControlFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # show the background image bg2.png from the resources folder in a label
        self.appPath = os.path.dirname(__file__)
        self.imagePath = os.path.join(self.appPath, "resources", "bg2.png")
        self.bg = tk.PhotoImage(file=self.imagePath, format="png")
        self.bgLabel = ttk.Label(self, image=self.bg)
        self.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        # add window title from constants file
        self.title(c.TITLE)
        self.geometry("700x700+50+50")
        self.resizable(False, False)

        # configure the one column of the grid view
        self.columnconfigure(index=0, weight=1)

        # add a title label containing the title message
        self.titleLabel = ttk.Label(self, text=c.TITLE_LABEL, font=("Futura", 20))
        self.titleLabel.grid(column=0, row=0, pady=40)


if __name__ == "__main__":
    # start the main window specified above
    app = App()

    # place the control frame inside the window
    ControlFrame(app)

    # call tkinter mainloop of the main window
    app.mainloop()

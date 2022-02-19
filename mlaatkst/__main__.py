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

import tkinter as tk
from tkinter import ttk

from mlaatkst.control_frame import ControlFrame
from mlaatkst.language_helper import LanguageHelper
from mlaatkst.menubar import Menubar
from mlaatkst.resource_helper import ResourceHelper

# choose the right constants file depending on the language
if LanguageHelper.get_lang() == "GER":
    import mlaatkst.constants_de as c
elif LanguageHelper.get_lang() == "ENG":
    import mlaatkst.constants_eng as c


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # show the background image bg2.png from the resources folder in a label
        self.bg_path = ResourceHelper.get_resource_path("bg2.png")
        self.bg = tk.PhotoImage(file=self.bg_path, format="png")
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


def main():
    # start the main window specified above
    app = App()

    # add menubar
    Menubar(app)

    # place the control frame inside the window
    ControlFrame(app)

    # call tkinter mainloop of the main window
    app.mainloop()


if __name__ == "__main__":
    main()

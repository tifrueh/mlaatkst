# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the Menubar class which is responsible for showing the correct menus lives here
import tkinter as tk

from mlaatkst.language_helper import LanguageHelper
from mlaatkst.settings_window import SettingsWindow

# choose the right constants file depending on the language
if LanguageHelper.get_lang() == "GER":
    import mlaatkst.constants_de as c
elif LanguageHelper.get_lang() == "ENG":
    import mlaatkst.constants_eng as c


class Menubar(tk.Menu):
    def __init__(self, container):
        super().__init__(container)

        self.container = container

        # set this menubar to be the menubar of the containing object
        container.config(menu=self)

        # start new menu
        self.settings_menu = tk.Menu(self, tearoff=False)

        # add command to menu which opens a settings window
        self.settings_menu.add_command(
            label=c.OPEN_SETTINGS_TITLE,
            command=self.open_settings
        )

        # add menu with correct title to menubar
        self.add_cascade(
            label=c.SETTINGS_TITLE,
            menu=self.settings_menu
        )

    # method for opening a settings window
    def open_settings(self):
        SettingsWindow(self.container)

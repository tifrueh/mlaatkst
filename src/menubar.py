import tkinter as tk
from language_helper import LanguageHelper
from settings_window import SettingsWindow

if LanguageHelper.get_lang() == "GER":
    import constants_de as c
elif LanguageHelper.get_lang() == "ENG":
    import constants_eng as c


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
            label="Open settings window",
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
# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the SettingsWindow class which shows a settings window lives here
import tkinter as tk
from tkinter import ttk

from mlaatkst.language_helper import LanguageHelper

# choose the right constants file depending on the language
if LanguageHelper.get_lang() == "GER":
    import mlaatkst.constants_de as c
elif LanguageHelper.get_lang() == "ENG":
    import mlaatkst.constants_eng as c


class SettingsWindow(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container)

        self.container = container

        # set geometry and window title
        self.geometry("300x200+100+100")
        self.title(c.SETTINGS_TITLE)

        # call grab_set for window to receive events
        # and to prevent user interaction with main window
        self.grab_set()

        # initiate a title label, two buttons (to change the language)
        # and finally a note
        self.label = ttk.Label(self, text=c.SETTINGS_LABEL)
        self.gerButton = ttk.Button(self, text=c.GERMAN, command=self.set_ger)
        self.engButton = ttk.Button(self, text=c.ENGLISH, command=self.set_eng)
        self.note = ttk.Label(self, text=c.SETTINGS_NOTE, wraplength=200, font="Helvetica 12 italic")

        # display everything on the window
        self.label.pack(pady=10)
        self.gerButton.pack()
        self.engButton.pack()
        self.note.pack(pady=20)

    # method for setting the language to German and closing the program afterwards
    def set_ger(self):
        LanguageHelper.set_lang("GER")
        self.destroy()
        self.container.destroy()

    # method for setting the language to English and closing the program afterwards
    def set_eng(self):
        LanguageHelper.set_lang("ENG")
        self.destroy()
        self.container.destroy()

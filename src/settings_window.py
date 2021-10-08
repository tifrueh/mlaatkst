import tkinter as tk
from tkinter import ttk
from language_helper import LanguageHelper

if LanguageHelper.get_lang() == "GER":
    import constants_de as c
elif LanguageHelper.get_lang() == "ENG":
    import constants_eng as c


class SettingsWindow(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container)

        self.geometry("300x200+100+100")
        self.title(c.SETTINGS_TITLE)

        self.label = ttk.Label(self, text=c.SETTINGS_LABEL)
        self.gerButton = ttk.Button(self, text=c.GERMAN, command=self.set_ger)
        self.engButton = ttk.Button(self, text=c.ENGLISH, command=self.set_eng)
        self.note = ttk.Label(self, text=c.SETTINGS_NOTE, wraplength=200, font="Helvetica 12 italic")

        self.label.pack(pady=10)
        self.gerButton.pack()
        self.engButton.pack()
        self.note.pack(pady=20)

    def set_ger(self):
        LanguageHelper.set_lang("GER")

    def set_eng(self):
        LanguageHelper.set_lang("ENG")

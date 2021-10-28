# Copyright (C) 2021  Timo Früh
# full copyright notice in main.py

# the ControlFrame class which draws the control frame lives here

import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from language_helper import LanguageHelper

# choose the right constants file depending on the language
if LanguageHelper.get_lang() == "GER":
    import constants_de as c
elif LanguageHelper.get_lang() == "ENG":
    import constants_eng as c


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)

        # set the title of the frame
        self["text"] = c.CONTROL_FRAME_TITLE

        # initialize empty integer which later determines
        # which frame should be raised
        self.selectedFrame = tk.IntVar()

        # make radiobuttons (the variable of which is selectedFrame) and place them on the grid of this frame
        # through which the user can decide on the frame to be shown
        ttk.Radiobutton(
            self,
            text=c.BOOK_BUTTON,
            value=0,
            variable=self.selectedFrame,
            command=self.change_frame
        ).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text=c.SCNDBOOK_BUTTON,
            value=1,
            variable=self.selectedFrame,
            command=self.change_frame
        ).grid(column=1, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text=c.WEB_BUTTON,
            value=2,
            variable=self.selectedFrame,
            command=self.change_frame
        ).grid(column=2, row=0, padx=5, pady=5)

        # put this option frame on the grid of the containing object
        self.grid(column=0, row=1, padx=50, pady=0, sticky=tk.NSEW)

        # make all needed frames and place them in a set
        self.frames = {0: EntryFrame(
            container,
            "book"
        ), 1: EntryFrame(
            container,
            "scndBook"
        ), 2: EntryFrame(
            container,
            "web"
        )}

        # call the change_frame function to raise the correct frame
        self.change_frame()

    def change_frame(self):

        # look which frame was chosen by the user
        # and assign it to the frame variable
        frame = self.frames[self.selectedFrame.get()]

        # reset the chosen frame
        frame.reset()

        # raise the chosen frame to the top
        frame.tkraise()

import tkinter as tk
import constants as c
from tkinter import ttk
from EntryFrame import EntryFrame

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self["text"] = "Optionen"

        self.selectedFrame = tk.IntVar()

        ttk.Radiobutton(
            self,
            text=c.BOOK_BUTTON,
            value=0,
            variable=self.selectedFrame,
            command=self.changeFrame
        ).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text=c.SCNDBOOK_BUTTON,
            value=1,
            variable=self.selectedFrame,
            command=self.changeFrame
        ).grid(column=1, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text=c.WEB_BUTTON,
            value=2,
            variable=self.selectedFrame,
            command=self.changeFrame
        ).grid(column=2, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=30, pady=30, sticky=tk.NSEW)

        self.frames = {}
        self.frames[0] = EntryFrame(
            container,
            "book"
        )
        self.frames[1] = EntryFrame(
            container,
            "scndBook"
        )
        self.frames[2] = EntryFrame(
            container,
            "web"
        )

        self.changeFrame()

    def changeFrame(self):
        frame = self.frames[self.selectedFrame.get()]
        frame.lastNameAuthorEntry.focus()
        frame.nameAuthorEntry.focus()
        frame.reset()
        frame.tkraise()
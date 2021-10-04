import tkinter as tk
import constants as c
from tkinter import ttk
from CitationFormatter import CitationFormatter

class BookFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        
        self.nameAuthor = tk.StringVar()
        self.title = tk.StringVar()
        self.subtitle = tk.StringVar()
        self.edition = tk.StringVar()
        self.publisher = tk.StringVar()
        self.location = tk.StringVar()
        self.year = tk.StringVar()
        self.pageS = tk.StringVar()

        self.authorLabel = ttk.Label(self, text=c.AUTHOR_PROMPT).pack()
        self.authorEntry = ttk.Entry(self, textvariable=self.nameAuthor).pack()

        self.titleLabel = ttk.Label(self, text=c.TITLE_PROMPT).pack()
        self.titleEntry = ttk.Entry(self, textvariable=self.title).pack()

        self.subtitleLabel = ttk.Label(self, text=c.SUBTITLE_PROMPT).pack()
        self.subtitleEntry = ttk.Entry(self, textvariable=self.subtitle).pack()

        self.editionLabel = ttk.Label(self, text=c.EDITION_PROMPT).pack()
        self.editionEntry = ttk.Entry(self, textvariable=self.edition).pack()

        self.publisherLabel = ttk.Label(self, text=c.PUBLISHER_PROMPT).pack()
        self.publisherEntry = ttk.Entry(self, textvariable=self.publisher).pack()

        self.locationLabel = ttk.Label(self, text=c.LOCATION_PROMPT).pack()
        self.locationEntry = ttk.Entry(self, textvariable=self.location).pack()

        self.yearLabel = ttk.Label(self, text=c.YEAR_PROMPT).pack()
        self.yearEntry = ttk.Entry(self, textvariable=self.year).pack()

        self.pageSLabel = ttk.Label(self, text=c.PAGES_PROMPT).pack()
        self.pageSEntry = ttk.Entry(self, textvariable=self.pageS).pack()

        self.enterButton = ttk.Button(self, text="Fertig", command=self.format).pack()

        self.resultLabel = ttk.Label(self).pack()

    def format(self):
        result = CitationFormatter.book(self.nameAuthor, self.title, self.subtitle, self.edition, self.publisher, self.location, self.year, self.pageS)
        self.resultLabel.config(text=result)

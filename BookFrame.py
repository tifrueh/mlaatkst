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

        self.authorLabel = ttk.Label(self, text=c.AUTHOR_PROMPT, justify=tk.CENTER)
        self.authorLabel.pack()
        self.authorEntry = ttk.Entry(self, textvariable=self.nameAuthor)
        self.authorEntry.pack()

        self.titleLabel = ttk.Label(self, text=c.TITLE_PROMPT, justify=tk.CENTER)
        self.titleLabel.pack()
        self.titleEntry = ttk.Entry(self, textvariable=self.title)
        self.titleEntry.pack()

        self.subtitleLabel = ttk.Label(self, text=c.SUBTITLE_PROMPT, justify=tk.CENTER)
        self.subtitleLabel.pack()
        self.subtitleEntry = ttk.Entry(self, textvariable=self.subtitle)
        self.subtitleEntry.pack()

        self.editionLabel = ttk.Label(self, text=c.EDITION_PROMPT, justify=tk.CENTER)
        self.editionLabel.pack()
        self.editionEntry = ttk.Entry(self, textvariable=self.edition)
        self.editionEntry.pack()

        self.publisherLabel = ttk.Label(self, text=c.PUBLISHER_PROMPT, justify=tk.CENTER)
        self.publisherLabel.pack()
        self.publisherEntry = ttk.Entry(self, textvariable=self.publisher)
        self.publisherEntry.pack()

        self.locationLabel = ttk.Label(self, text=c.LOCATION_PROMPT, justify=tk.CENTER)
        self.locationLabel.pack()
        self.locationEntry = ttk.Entry(self, textvariable=self.location)
        self.locationEntry.pack()

        self.yearLabel = ttk.Label(self, text=c.YEAR_PROMPT, justify=tk.CENTER)
        self.yearLabel.pack()
        self.yearEntry = ttk.Entry(self, textvariable=self.year)
        self.yearEntry.pack()

        self.pageSLabel = ttk.Label(self, text=c.PAGES_PROMPT, justify=tk.CENTER)
        self.pageSLabel.pack()
        self.pageSEntry = ttk.Entry(self, textvariable=self.pageS)
        self.pageSEntry.pack()

        self.enterButton = ttk.Button(self, text="Fertig", command=self.format)
        self.enterButton.pack()

        self.resultLabel = ttk.Label(self, justify=tk.CENTER)
        self.resultLabel.pack()

        self.pack()

    def format(self):
        result = CitationFormatter.book(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.edition.get(), self.publisher.get(), self.location.get(), self.year.get(), self.pageS.get())
        self.resultLabel.config(text=result)

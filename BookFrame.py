import clipboard
import tkinter as tk
import constants as c
from tkinter.constants import W
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

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)

        self.authorLabel = ttk.Label(self, text=c.AUTHOR_PROMPT, justify=tk.LEFT)
        self.authorLabel.grid(column=0, row=0, sticky=tk.W, padx=10)
        self.authorEntry = ttk.Entry(self, textvariable=self.nameAuthor)
        self.authorEntry.grid(column=1, row=0, pady=10, padx=10)

        self.titleLabel = ttk.Label(self, text=c.TITLE_PROMPT, justify=tk.LEFT)
        self.titleLabel.grid(column=0, row=1, sticky=tk.W, padx=10)
        self.titleEntry = ttk.Entry(self, textvariable=self.title)
        self.titleEntry.grid(column=1, row=1, pady=10, padx=10)

        self.subtitleLabel = ttk.Label(self, text=c.SUBTITLE_PROMPT, justify=tk.LEFT)
        self.subtitleLabel.grid(column=0, row=2, sticky=tk.W, padx=10)
        self.subtitleEntry = ttk.Entry(self, textvariable=self.subtitle)
        self.subtitleEntry.grid(column=1, row=2, pady=10, padx=10)

        self.editionLabel = ttk.Label(self, text=c.EDITION_PROMPT, justify=tk.LEFT)
        self.editionLabel.grid(column=0, row=3, sticky=tk.W, padx=10)
        self.editionEntry = ttk.Entry(self, textvariable=self.edition)
        self.editionEntry.grid(column=1, row=3, pady=10, padx=10)

        self.publisherLabel = ttk.Label(self, text=c.PUBLISHER_PROMPT, justify=tk.LEFT)
        self.publisherLabel.grid(column=0, row=4, sticky=tk.W, padx=10)
        self.publisherEntry = ttk.Entry(self, textvariable=self.publisher)
        self.publisherEntry.grid(column=1, row=4, pady=10, padx=10)

        self.locationLabel = ttk.Label(self, text=c.LOCATION_PROMPT, justify=tk.LEFT)
        self.locationLabel.grid(column=0, row=5, sticky=tk.W, padx=10)
        self.locationEntry = ttk.Entry(self, textvariable=self.location)
        self.locationEntry.grid(column=1, row=5, pady=10, padx=10)

        self.yearLabel = ttk.Label(self, text=c.YEAR_PROMPT, justify=tk.LEFT)
        self.yearLabel.grid(column=0, row=6, sticky=tk.W, padx=10)
        self.yearEntry = ttk.Entry(self, textvariable=self.year)
        self.yearEntry.grid(column=1, row=6, pady=10, padx=10)

        self.pageSLabel = ttk.Label(self, text=c.PAGES_PROMPT, justify=tk.LEFT)
        self.pageSLabel.grid(column=0, row=7, sticky=tk.W, padx=10)
        self.pageSEntry = ttk.Entry(self, textvariable=self.pageS)
        self.pageSEntry.grid(column=1, row=7, pady=10, padx=10)

        self.enterButton = ttk.Button(self, text="Fertig", command=self.formatCitation)
        self.enterButton.grid(columnspan=2, row=8, pady=20)

        self.resultLabel = ttk.Label(self, justify=tk.LEFT, text="Resultat erscheint hier...")
        self.resultLabel.grid(columnspan=2, row=9, padx=20, pady=5)

        self.copyButton = ttk.Button(self, text="Kopieren", command=self.copyCitation)
        self.copyButton.grid(columnspan=2, row=10)

        self.pack(fill="x", padx=20, pady=10)

    def formatCitation(self):
        result = CitationFormatter.book(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.edition.get(), self.publisher.get(), self.location.get(), self.year.get(), self.pageS.get())
        self.resultLabel.config(text=result)
    
    def copyCitation(self):
        result = CitationFormatter.book(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.edition.get(), self.publisher.get(), self.location.get(), self.year.get(), self.pageS.get())
        clipboard.copy(result)
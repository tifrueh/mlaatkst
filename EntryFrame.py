import clipboard
import tkinter as tk
import constants as c
from tkinter import ttk
from CitationFormatter import CitationFormatter

class BookFrame(ttk.LabelFrame):
    def __init__(self, container, option):
        super().__init__(container)

        self.option = option
        self.nameAuthor = tk.StringVar()
        self.lastNameAuthor = tk.StringVar()
        self.title = tk.StringVar()
        self.subtitle = tk.StringVar()
        self.edition = tk.StringVar()
        self.publisher = tk.StringVar()
        self.location = tk.StringVar()
        self.year = tk.StringVar()
        self.pageS = tk.StringVar()
        self.url = tk.StringVar()
        self.downDate = tk.StringVar()

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)

        if self.option == "book" or self.option == "web":
            self.askAuthor()
        
        if self.option == "scndBook":
            self.askLastNameAuthor()

        if self.option == "book" or self.option == "web":
            self.askTitle()

        if self.option == "book" or self.option == "web":
            self.askSubtitle()

        if self.option == "book":
            self.askEdition()

        if self.option == "book":
            self.askPublisher()

        if self.option == "book":
            self.askLocation()

        if self.option == "book" or self.option == "scndBook":
            self.askYear()
        
        if self.option == "book" or self.option == "scndBook":
            self.askPageS()
        
        if self.option == "web":
            self.askURL()
        
        if self.option == "web":
            self.askDownDate()

        self.enterButton = ttk.Button(self, text="Fertig", command=self.formatCitation)
        self.enterButton.grid(columnspan=2, row=11, pady=20)

        self.resultLabel = ttk.Label(self, justify=tk.LEFT, text="Resultat erscheint hier...")
        self.resultLabel.grid(columnspan=2, row=12, padx=20, pady=5)

        self.copyButton = ttk.Button(self, text="Kopieren", command=self.copyCitation)
        self.copyButton.grid(columnspan=2, row=13)

        self.pack(fill="x", padx=20, pady=10)

    def formatCitation(self):
        result = CitationFormatter.book(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.edition.get(), self.publisher.get(), self.location.get(), self.year.get(), self.pageS.get())
        self.resultLabel.config(text=result)
    
    def copyCitation(self):
        result = CitationFormatter.book(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.edition.get(), self.publisher.get(), self.location.get(), self.year.get(), self.pageS.get())
        clipboard.copy(result)
    
    def askAuthor(self):
        self.authorLabel = ttk.Label(self, text=c.AUTHOR_PROMPT, justify=tk.LEFT)
        self.authorLabel.grid(column=0, row=0, sticky=tk.W, padx=10)
        self.authorEntry = ttk.Entry(self, textvariable=self.nameAuthor)
        self.authorEntry.grid(column=1, row=0, pady=10, padx=10)
    
    def askLastNameAuthor(self):
        self.authorLastNameLabel = ttk.Label(self, text=c.AUTHOR_LASTNAME_PROMPT, justify=tk.LEFT)
        self.authorLastNameLabel.grid(column=0, row=1, sticky=tk.W, padx=10)
        self.authorLastNameEntry = ttk.Entry(self, textvariable=self.lastNameAuthor)
        self.authorLastNameEntry.grid(column=1, row=1, pady=10, padx=10)

    def askTitle(self):
        self.titleLabel = ttk.Label(self, text=c.TITLE_PROMPT, justify=tk.LEFT)
        self.titleLabel.grid(column=0, row=2, sticky=tk.W, padx=10)
        self.titleEntry = ttk.Entry(self, textvariable=self.title)
        self.titleEntry.grid(column=1, row=2, pady=10, padx=10)
    
    def askSubtitle(self):
        self.subtitleLabel = ttk.Label(self, text=c.SUBTITLE_PROMPT, justify=tk.LEFT)
        self.subtitleLabel.grid(column=0, row=3, sticky=tk.W, padx=10)
        self.subtitleEntry = ttk.Entry(self, textvariable=self.subtitle)
        self.subtitleEntry.grid(column=1, row=3, pady=10, padx=10)
    
    def askEdition(self):
        self.editionLabel = ttk.Label(self, text=c.EDITION_PROMPT, justify=tk.LEFT)
        self.editionLabel.grid(column=0, row=3, sticky=tk.W, padx=10)
        self.editionEntry = ttk.Entry(self, textvariable=self.edition)
        self.editionEntry.grid(column=1, row=3, pady=10, padx=10)
    
    def askPublisher(self):
        self.publisherLabel = ttk.Label(self, text=c.PUBLISHER_PROMPT, justify=tk.LEFT)
        self.publisherLabel.grid(column=0, row=4, sticky=tk.W, padx=10)
        self.publisherEntry = ttk.Entry(self, textvariable=self.publisher)
        self.publisherEntry.grid(column=1, row=4, pady=10, padx=10)
    
    def askLocation(self):
        self.locationLabel = ttk.Label(self, text=c.LOCATION_PROMPT, justify=tk.LEFT)
        self.locationLabel.grid(column=0, row=5, sticky=tk.W, padx=10)
        self.locationEntry = ttk.Entry(self, textvariable=self.location)
        self.locationEntry.grid(column=1, row=5, pady=10, padx=10)
    
    def askYear(self):
        self.yearLabel = ttk.Label(self, text=c.YEAR_PROMPT, justify=tk.LEFT)
        self.yearLabel.grid(column=0, row=6, sticky=tk.W, padx=10)
        self.yearEntry = ttk.Entry(self, textvariable=self.year)
        self.yearEntry.grid(column=1, row=6, pady=10, padx=10)
    
    def askPageS(self):
        self.pageSLabel = ttk.Label(self, text=c.PAGES_PROMPT, justify=tk.LEFT)
        self.pageSLabel.grid(column=0, row=7, sticky=tk.W, padx=10)
        self.pageSEntry = ttk.Entry(self, textvariable=self.pageS)
        self.pageSEntry.grid(column=1, row=7, pady=10, padx=10)
    
    def askURL(self):
        self.urlLabel = ttk.Label(self, text=c.URL_PROMPT, justify=tk.LEFT)
        self.urlLabel.grid(column=0, row=9, sticky=tk.W, padx=10)
        self.urlEntry = ttk.Entry(self, textvariable=self.url)
        self.urlEntry.grid(column=1, row=9, pady=10, padx=10)
    
    def askDownDate(self):
        self.downDateLabel = ttk.Label(self, text=c.DOWNDATE_PROMPT, justify=tk.LEFT)
        self.downDateLabel.grid(column=0, row=7, sticky=tk.W, padx=10)
        self.downDateEntry = ttk.Entry(self, textvariable=self.downDate)
        self.downDateEntry.grid(column=1, row=7, pady=10, padx=10)
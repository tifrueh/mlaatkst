import clipboard
import tkinter as tk
import constants as c
from tkinter import ttk
from CitationFormatter import CitationFormatter

class EntryFrame(ttk.Frame):
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

        self.nameAuthorLabel = ttk.Label(self, text=c.AUTHOR_PROMPT, justify=tk.LEFT)
        self.nameAuthorEntry = ttk.Entry(self, textvariable=self.nameAuthor)
        self.lastNameAuthorLabel = ttk.Label(self, text=c.AUTHOR_LASTNAME_PROMPT, justify=tk.LEFT)
        self.lastNameAuthorEntry = ttk.Entry(self, textvariable=self.lastNameAuthor)
        self.titleLabel = ttk.Label(self, text=c.TITLE_PROMPT, justify=tk.LEFT)
        self.titleEntry = ttk.Entry(self, textvariable=self.title)
        self.subtitleLabel = ttk.Label(self, text=c.SUBTITLE_PROMPT, justify=tk.LEFT)
        self.subtitleEntry = ttk.Entry(self, textvariable=self.subtitle)
        self.editionLabel = ttk.Label(self, text=c.EDITION_PROMPT, justify=tk.LEFT)
        self.editionEntry = ttk.Entry(self, textvariable=self.edition)
        self.publisherLabel = ttk.Label(self, text=c.PUBLISHER_PROMPT, justify=tk.LEFT)
        self.publisherEntry = ttk.Entry(self, textvariable=self.publisher)
        self.locationLabel = ttk.Label(self, text=c.LOCATION_PROMPT, justify=tk.LEFT)
        self.locationEntry = ttk.Entry(self, textvariable=self.location)
        self.yearLabel = ttk.Label(self, text=c.YEAR_PROMPT, justify=tk.LEFT)
        self.yearEntry = ttk.Entry(self, textvariable=self.year)
        self.pageSLabel = ttk.Label(self, text=c.PAGES_PROMPT, justify=tk.LEFT)
        self.pageSEntry = ttk.Entry(self, textvariable=self.pageS)
        self.urlLabel = ttk.Label(self, text=c.URL_PROMPT, justify=tk.LEFT)
        self.urlEntry = ttk.Entry(self, textvariable=self.url)
        self.downDateLabel = ttk.Label(self, text=c.DOWNDATE_PROMPT, justify=tk.LEFT)
        self.downDateEntry = ttk.Entry(self, textvariable=self.downDate)

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

        self.grid(column=0, row=1, sticky=tk.NSEW, padx=20, pady=10)

    def formatCitation(self):
        if self.option == "book":
            result = CitationFormatter.book(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.edition.get(), self.publisher.get(), self.location.get(), self.year.get(), self.pageS.get())
        elif self.option == "scndBook":
            result = CitationFormatter.scndBook(self.lastNameAuthor.get(), self.year.get(), self.pageS.get())
        elif self.option == "web":
            result = CitationFormatter.web(self.nameAuthor.get(), self.title.get(), self.subtitle.get(), self.url.get(), self.downDate.get())
        self.resultLabel.config(text=result)
    
    def copyCitation(self):
        citation = self.resultLabel["text"]
        clipboard.copy(citation)
    
    def reset(self):
        self.nameAuthorEntry.delete(0, tk.END)
        self.lastNameAuthorEntry.delete(0, tk.END)
        self.titleEntry.delete(0, tk.END)
        self.subtitleEntry.delete(0, tk.END)
        self.editionEntry.delete(0, tk.END)
        self.publisherEntry.delete(0, tk.END)
        self.locationEntry.delete(0, tk.END)
        self.yearEntry.delete(0, tk.END)
        self.pageSEntry.delete(0, tk.END)
        self.urlEntry.delete(0, tk.END)
        self.downDateEntry.delete(0, tk.END)
        self.resultLabel["text"] = "Resultat erscheint hier..."

    def askAuthor(self):
        self.nameAuthorLabel.grid(column=0, row=0, sticky=tk.W, padx=10)
        self.nameAuthorEntry.grid(column=1, row=0, pady=10, padx=10)
    
    def askLastNameAuthor(self):
        self.lastNameAuthorLabel.grid(column=0, row=1, sticky=tk.W, padx=10)
        self.lastNameAuthorEntry.grid(column=1, row=1, pady=10, padx=10)

    def askTitle(self):
        self.titleLabel.grid(column=0, row=2, sticky=tk.W, padx=10)
        self.titleEntry.grid(column=1, row=2, pady=10, padx=10)
    
    def askSubtitle(self):
        self.subtitleLabel.grid(column=0, row=3, sticky=tk.W, padx=10)
        self.subtitleEntry.grid(column=1, row=3, pady=10, padx=10)
    
    def askEdition(self):
        self.editionLabel.grid(column=0, row=4, sticky=tk.W, padx=10)
        self.editionEntry.grid(column=1, row=4, pady=10, padx=10)
    
    def askPublisher(self):
        self.publisherLabel.grid(column=0, row=5, sticky=tk.W, padx=10)
        self.publisherEntry.grid(column=1, row=5, pady=10, padx=10)
    
    def askLocation(self):
        self.locationLabel.grid(column=0, row=6, sticky=tk.W, padx=10)
        self.locationEntry.grid(column=1, row=6, pady=10, padx=10)
    
    def askYear(self):
        self.yearLabel.grid(column=0, row=7, sticky=tk.W, padx=10)
        self.yearEntry.grid(column=1, row=7, pady=10, padx=10)
    
    def askPageS(self):
        self.pageSLabel.grid(column=0, row=8, sticky=tk.W, padx=10)
        self.pageSEntry.grid(column=1, row=8, pady=10, padx=10)
    
    def askURL(self):
        self.urlLabel.grid(column=0, row=9, sticky=tk.W, padx=10)
        self.urlEntry.grid(column=1, row=9, pady=10, padx=10)
    
    def askDownDate(self):
        self.downDateLabel.grid(column=0, row=10, sticky=tk.W, padx=10)
        self.downDateEntry.grid(column=1, row=10, pady=10, padx=10)
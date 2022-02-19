# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the EntryFrame class which draws the entry frame lives here

import pyperclip as pyperclip
import tkinter as tk
from tkinter import ttk
from mlaatkst.citation_formatter import CitationFormatter
from mlaatkst.language_helper import LanguageHelper


class EntryFrame(ttk.Frame):
    def __init__(self, container: tk.Tk, option):
        super().__init__(container)

        # choose the right constants file depending on the language
        if LanguageHelper.get_lang() == "GER":
            import mlaatkst.constants_de as c
        else:
            import mlaatkst.constants_eng as c

        # initialize option variable
        # through which the control frame tells the program which frame to show
        self.option = option

        # initialize all needed variables
        # and set them to empty strings
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

        self.result = tk.StringVar()

        # initialize all possible labels and entries
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

        # configure the grid view
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=0)

        # choose which frames and entries to show
        # based on the value of the option variable
        if self.option == "book" or self.option == "web":
            self.ask_author()

        if self.option == "scndBook":
            self.ask_last_name_author()

        if self.option == "book" or self.option == "web":
            self.ask_title()

        if self.option == "book" or self.option == "web":
            self.ask_subtitle()

        if self.option == "book":
            self.ask_edition()

        if self.option == "book":
            self.ask_publisher()

        if self.option == "book":
            self.ask_location()

        if self.option == "book" or self.option == "scndBook":
            self.ask_year()

        if self.option == "book" or self.option == "scndBook":
            self.ask_page_s()

        if self.option == "web":
            self.ask_url()

        if self.option == "web":
            self.ask_down_date()

        # initialize label for result and set it to a standard message
        self.resultLabel = ttk.Label(self, justify=tk.LEFT, text=c.STANDARD_OUTPUT, wraplength=300)
        self.resultLabel.grid(column=0, row=11, sticky=tk.W, padx=10, pady=5)

        # place a button at the bottom which starts the formatting of the citation
        self.doneButton = ttk.Button(self, text=c.DONE_BUTTON, command=self.format_citation)
        self.doneButton.grid(column=1, row=11, sticky=tk.EW, padx=10, pady=20)

        # place another button under the doneButton which copies the formatted citation
        self.copyButton = ttk.Button(self, text=c.COPY_BUTTON, command=self.copy_citation)
        self.copyButton.grid(column=1, row=12, sticky=tk.EW, padx=10, pady=0)

        # place yet another button under the copyButton which clears out the entries
        self.resetButton = ttk.Button(self, text=c.RESET_BUTTON, command=self.reset)
        self.resetButton.grid(column=1, row=13, sticky=tk.EW, padx=10, pady=5)

        # place this whole entry frame on the grid of the containing object
        self.grid(column=0, row=2, sticky=tk.NSEW, padx=50, pady=5)

    def format_citation(self):

        # choose the formatter based on the value of the option variable
        # and based on the set language
        if self.option == "book":
            if LanguageHelper.get_lang() == "GER":
                self.result = CitationFormatter.book_ger(self.nameAuthor.get(),
                                                         self.title.get(),
                                                         self.subtitle.get(),
                                                         self.edition.get(),
                                                         self.publisher.get(),
                                                         self.location.get(),
                                                         self.year.get(),
                                                         self.pageS.get())
            elif LanguageHelper.get_lang() == "ENG":
                self.result = CitationFormatter.book_eng(self.nameAuthor.get(),
                                                         self.title.get(),
                                                         self.subtitle.get(),
                                                         self.edition.get(),
                                                         self.publisher.get(),
                                                         self.location.get(),
                                                         self.year.get(),
                                                         self.pageS.get())

        elif self.option == "scndBook":
            if LanguageHelper.get_lang() == "GER":
                self.result = CitationFormatter.scnd_book_ger(self.lastNameAuthor.get(),
                                                              self.year.get(),
                                                              self.pageS.get())
            elif LanguageHelper.get_lang() == "ENG":
                self.result = CitationFormatter.scnd_book_eng(self.lastNameAuthor.get(),
                                                              self.year.get(),
                                                              self.pageS.get())

        elif self.option == "web":
            self.result = CitationFormatter.web(self.nameAuthor.get(),
                                                self.title.get(),
                                                self.subtitle.get(),
                                                self.url.get(),
                                                self.downDate.get())

        # set the text of the prevously initialized resultLabel
        # to the result of the formatting
        self.resultLabel.config(text=self.result)

    def copy_citation(self):

        # copy the contents of the resultLabel
        citation = self.resultLabel["text"]
        pyperclip.copy(citation)

    def reset(self):

        # choose the right constants file depending on the language
        if LanguageHelper.get_lang() == "GER":
            import mlaatkst.constants_de as c
        else:
            import mlaatkst.constants_eng as c

        # clear out all entries
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

        # reset the resultLabel back to the standard message
        self.resultLabel["text"] = c.STANDARD_OUTPUT

        # set the keyboard focus back to the first entry
        self.lastNameAuthorEntry.focus_set()
        self.nameAuthorEntry.focus_set()

# methods for placing the prevously initialized labels and entries on the grid of the frame
    def ask_author(self):
        self.nameAuthorLabel.grid(column=0, row=0, sticky=tk.EW, padx=10)
        self.nameAuthorEntry.grid(column=1, row=0, sticky=tk.EW, pady=7, padx=10)

    def ask_last_name_author(self):
        self.lastNameAuthorLabel.grid(column=0, row=1, sticky=tk.EW, padx=10)
        self.lastNameAuthorEntry.grid(column=1, row=1, sticky=tk.EW, pady=7, padx=10)

    def ask_title(self):
        self.titleLabel.grid(column=0, row=2, sticky=tk.EW, padx=10)
        self.titleEntry.grid(column=1, row=2, sticky=tk.EW, pady=7, padx=10)

    def ask_subtitle(self):
        self.subtitleLabel.grid(column=0, row=3, sticky=tk.EW, padx=10)
        self.subtitleEntry.grid(column=1, row=3, sticky=tk.EW, pady=7, padx=10)

    def ask_edition(self):
        self.editionLabel.grid(column=0, row=4, sticky=tk.EW, padx=10)
        self.editionEntry.grid(column=1, row=4, sticky=tk.EW, pady=7, padx=10)

    def ask_publisher(self):
        self.publisherLabel.grid(column=0, row=5, sticky=tk.W, padx=10)
        self.publisherEntry.grid(column=1, row=5, sticky=tk.EW, pady=7, padx=10)

    def ask_location(self):
        self.locationLabel.grid(column=0, row=6, sticky=tk.EW, padx=10)
        self.locationEntry.grid(column=1, row=6, sticky=tk.EW, pady=7, padx=10)

    def ask_year(self):
        self.yearLabel.grid(column=0, row=7, sticky=tk.EW, padx=10)
        self.yearEntry.grid(column=1, row=7, sticky=tk.EW, pady=7, padx=10)

    def ask_page_s(self):
        self.pageSLabel.grid(column=0, row=8, sticky=tk.EW, padx=10)
        self.pageSEntry.grid(column=1, row=8, sticky=tk.EW, pady=7, padx=10)

    def ask_url(self):
        self.urlLabel.grid(column=0, row=9, sticky=tk.EW, padx=10)
        self.urlEntry.grid(column=1, row=9, sticky=tk.EW, pady=7, padx=10)

    def ask_down_date(self):
        self.downDateLabel.grid(column=0, row=10, sticky=tk.EW, padx=10)
        self.downDateEntry.grid(column=1, row=10, sticky=tk.EW, pady=7, padx=10)

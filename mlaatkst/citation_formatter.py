# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the CitationFormatter class which formats the citations lives here

class CitationFormatter:

    # define the method for formatting a citation of a book in german
    @staticmethod
    def book_ger(name_author, title, subtitle, edition, publisher, location, year, pages):

        # omit subtitle if empty
        if subtitle == "" or subtitle == " ":
            result = f"{name_author}, {title}, {edition}. Auflage, " \
                     f"{publisher}, {location}, {year}, S. {pages}."
        else:
            result = f"{name_author}, {title}, {subtitle}, {edition}. Auflage, " \
                     f"{publisher}, {location}, {year}, S. {pages}. "

        return result

    # define the method for formatting a citation of a book in english
    @staticmethod
    def book_eng(name_author, title, subtitle, edition, publisher, location, year, pages):

        # omit subtitle if empty
        if subtitle == "" or subtitle == " ":
            result = f"{name_author}, {title}, {edition}. edition, " \
                     f"{publisher}, {location}, {year}, p. {pages}."
        else:
            result = f"{name_author}, {title}, {subtitle}, {edition}. edition, " \
                     f"{publisher}, {location}, {year}, p. {pages}. "

        return result

    # define the method for formatting the second citation of a book
    @staticmethod
    def scnd_book_ger(last_name_author, year, pages):
        result = f"{last_name_author}, {year}, S. {pages}."

        return result

    # define the method for formatting the second citation of a book in english
    @staticmethod
    def scnd_book_eng(last_name_author, year, pages):
        result = f"{last_name_author}, {year}, p. {pages}."

        return result

    # define the method for formatting a citation of a website
    @staticmethod
    def web(name_author, title, subtitle, url, down_date):

        # omit subtitle if empty
        if subtitle == "" or subtitle == " ":
            result = f"{name_author}, {title}, {url}, {down_date}."
        else:
            result = f"{name_author}, {title}, {subtitle}, {url}, {down_date}."

        return result

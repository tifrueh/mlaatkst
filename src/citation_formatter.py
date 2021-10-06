class CitationFormatter:

    # define the method for formatting a citation of a book
    @staticmethod
    def book(nameauthor, title, subtitle, edition, publisher, location, year, pages):

        # omit subtitle if empty
        if subtitle == "" or subtitle == " ":
            result = f"{nameauthor}, {title}, {edition}. Auflage, {publisher}, {location}, {year}, S. {pages}."
        else:
            result = f"{nameauthor}, {title}, {subtitle}, {edition}. Auflage, {publisher}, {location}, {year}, S. {pages}. "

        return result

    # define the method for formatting the second citation of a book
    @staticmethod
    def scnd_book(lastnameauthor, year, pages):
        result = f"{lastnameauthor}, {year}, S. {pages}."

        return result

    # define the method for formatting a citation of a website
    @staticmethod
    def web(nameauthor, title, subtitle, url, downdate):

        # omit subtitle if empty
        if subtitle == "" or subtitle == " ":
            result = f"{nameauthor}, {title}, {url}, {downdate}."
        else:
            result = f"{nameauthor}, {title}, {subtitle}, {url}, {downdate}."

        return result

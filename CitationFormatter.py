class CitationFormatter:

    @staticmethod
    def book(nameauthor, title, subtitle, edition, publisher, location, year, pages):
        if subtitle == "" or subtitle == " ":
            result = f"{nameauthor}, {title}, {edition}. Auflage, {publisher}, {location}, {year}, S. {pages}."
        else:
            result = f"{nameauthor}, {title}, {subtitle}, {edition}. Auflage, {publisher}, {location}, {year}, S. {pages}. "

        return result

    @staticmethod
    def scnd_book(lastnameauthor, year, pages):
        result = f"{lastnameauthor}, {year}, S. {pages}."

        return result

    @staticmethod
    def web(nameauthor, title, subtitle, url, downdate):
        if subtitle == "" or subtitle == " ":
            result = f"{nameauthor}, {title}, {url}, {downdate}."
        else:
            result = f"{nameauthor}, {title}, {subtitle}, {url}, {downdate}."

        return result

class CitationFormatter:

    @staticmethod
    def book(nameAuthor, title, subtitle, edition, publisher, location, year, pageS):
        if subtitle == "" or subtitle == " ":
            result = f"{nameAuthor}, {title}, {edition}. Auflage, {publisher}, {location}, {year}, S. {pageS}."
        else:
            result = f"{nameAuthor}, {title}, {subtitle}, {edition}. Auflage, {publisher}, {location}, {year}, S. {pageS}."
        
        return result
    
    @staticmethod
    def scndBook(lastNameAuthor, year, pageS):
        result = f"{lastNameAuthor}, {year}, S. {pageS}."
        
        return result
    
    @staticmethod
    def web(nameAuthor, title, subtitle, url, downDate):
        if subtitle == "" or subtitle == " ":
            result = f"{nameAuthor}, {title}, {url}, {downDate}."
        else:
            result = f"{nameAuthor}, {title}, {subtitle}, {url}, {downDate}."
        
        return result
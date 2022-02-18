# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the LanguageHelper which helps to add language support lives here
from pkg_resources import resource_filename


class LanguageHelper:

    # method for getting the string contained in ./resources/lang.txt
    @staticmethod
    def get_lang():
        lang_path = resource_filename("mlaatkst.resources", "lang.txt")
        with open(lang_path, "r") as lang_file:
            lang = lang_file.read()
        return lang

    # method for setting the string contained in ./resources/lang.txt
    @staticmethod
    def set_lang(lang):
        lang_path = resource_filename("mlaatkst.resources", "lang.txt")
        with open(lang_path, "w") as lang_file:
            lang_file.write(lang)

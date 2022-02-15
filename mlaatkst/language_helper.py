# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the LanguageHelper which helps to add language support lives here
import os


class LanguageHelper:

    # method for getting the string contained in ./resources/lang.txt
    @staticmethod
    def get_lang():
        app_path = os.path.dirname(__file__)
        lang_path = os.path.join(app_path, "resources", "lang.txt")
        lang_file = open(lang_path, "r")
        lang = lang_file.read()
        return lang

    # method for setting the string contained in ./resources/lang.txt
    @staticmethod
    def set_lang(lang):
        app_path = os.path.dirname(__file__)
        lang_path = os.path.join(app_path, "resources", "lang.txt")
        lang_file = open(lang_path, "w")
        lang_file.write(lang)

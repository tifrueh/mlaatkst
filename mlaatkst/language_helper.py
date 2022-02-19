# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py

# the LanguageHelper which helps to add language support lives here
from mlaatkst.resource_helper import ResourceHelper


class LanguageHelper:

    # method for getting the string contained in ./resources/lang.txt
    @staticmethod
    def get_lang():
        lang = ResourceHelper.read_text_resource("lang.txt")
        return lang

    # method for setting the string contained in ./resources/lang.txt
    @staticmethod
    def set_lang(lang):
        ResourceHelper.write_text_resource("lang.txt", lang)

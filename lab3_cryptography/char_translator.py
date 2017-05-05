"""
This file contains code to generate the random substitution code and to 
translate and untranslate individual characters based on that code.
"""

import random
import string

def random_permute_chars():
    """ generates a random permutation of char in range a-z """
    l = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(l)
    return string.join(l, "")

class CharTranslator(string):
    def __init__(self, string):
        """ takes random a-z string and checks for valid permutation """
        self.string = string
        

    def translate_char(self):
        """ empty """

    def unstranslate_char(self):
        """ empty """

class InvalidTranslationString:
    def __init(self):
        """ empty """


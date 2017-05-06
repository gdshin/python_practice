"""
This file contains code to generate the random substitution code and to 
translate and untranslate individual characters based on that code.
"""

import random
import string
from collections import Counter

def random_permute_chars():
    """ generates a random permutation of char in range a-z """
    s = string.ascii_lowercase
    return ''.join(random.sample(s,len(s)))

class CharTranslator(string):
    def __init__(self, string):
        """ takes random a-z string and checks for valid permutation """
        if Counter(string) == Counter(string.ascii_lowercase):
            self.string = string
        else:
            raise Exception("Not a valid permutation of a-z string")

    def translate_char(self):
        """ empty """

    def unstranslate_char(self):
        """ empty """

class InvalidTranslationString:
    def __init(self):
        """ empty """


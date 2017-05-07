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

class CharTranslator:
    def __init__(self, input_str):
        """ takes random a-z string and checks for valid permutation """
        self.str_ordered = string.ascii_lowercase
        if Counter(self.str_ordered) == Counter(input_str):
            self.str_random = input_str
        else:
            raise InvalidTranslationString("Not a valid permutation of a-z string")

    def translate_char(self, char):
        """ translates a single character based on permutation """
        return self.convert_char(char, self.str_ordered, self.str_random)

    def untranslate_char(self, char):
        """ untranslates a single character based on permutation """
        return self.convert_char(char, self.str_random, self.str_ordered)

    def convert_char(self, char, a, b):
        if len(char) is not 1:
            raise Exception("Expect string len 1 not {}".format(str(len(char))))
        if char.isalpha():
            if char.isupper():
                """ convert uppercase """
                num_lower = ord(char) + 32
                char_lower = a.index(chr(num_lower))
                return b[char_lower].upper()
            else:
                return b[a.index(char)]
        else:
            return char

class InvalidTranslationString(Exception):
    pass


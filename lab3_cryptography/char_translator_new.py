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

        # variable with alphabet, a....z
        self.str_ordered = string.ascii_lowercase
        # attempt 1, not bad!
        '''
        if Counter(self.str_ordered) == Counter(input_str):
            self.str_random = input_str
        '''
        # More efficient, you don't have to create dictionaries
        # Dictionaries very efficient for lookup though have high memory overhead
        # Also not really needed for this, you don't need a frequency distribution
        # All letters only appear once
        if sorted(self.str_ordered) == sorted(input_str):
            self.str_random = input_str
            # _ before function means private method, i.e. it cannot be called outside the core class code
            self._create_mapping()
        else:
            raise InvalidTranslationString("Not a valid permutation of a-z str")

    # EXAMPLE OF A PRIVATE METHOD
    def _create_mapping(self):
        """ Create two mappings, to translate from original ordered to permutation, and to decode permutation back to original"""
        self.translate_mapping = dict()
        self.untranslate_mapping = dict()
        # count = 0; while count < 26; count++
        # Looping through the strings in tandem
        for i in range(len(self.str_ordered)):
            self.translate_mapping[self.str_ordered[i]] = self.str_random[i]
            self.untranslate_mapping[self.str_random[i]] = self.str_ordered[i]

    def translate_char(self, char):
        """ translates a single character based on permutation """
        # check to make sure the character is in the dictionary
        # Aside: cool dictionary hint, dict.values() returns a list of values in the dictionary
        # i.e. d = {'a':'b'}, d.values() = ['b']
        if char.lower() in self.translate_mapping:
            return self.translate_mapping[char]
        else:
            return char

    def untranslate_char(self, char):
        """ untranslates a single character based on permutation """
        if char.lower() in self.untranslate_mapping:
            return self.untranslate_mapping[char]
        else:
            return char

    # Original method: Correct
    # Inefficieny: every time we convert a character, we recalculate the mapping from a to b
    # We want to do just one time in the beginning
    ''':ta
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
    '''

class InvalidTranslationString(Exception):
    pass

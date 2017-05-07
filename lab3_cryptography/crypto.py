
"""
This file does the translation and untranslation of files.
"""

import char_translator

class Coder:
    """ takes a CharTranslator object as its argument and stores it """
    def __init__(self, ts_obj):
        self.obj = ts_obj

    """ takes an input and output file name and encodes the input file,
    storing the output in the output file. """
    def encode_file(self, in_file, out_file):
        self.file_conversion(in_file, out_file, self.obj.translate_char)

    """ takes an input and output file name and decodes the input file,
    storing the output in the output file. """
    def decode_file(self, in_file, out_file):
        self.file_conversion(in_file, out_file, self.obj.untranslate_char)

    """ file conversion of in_file to out_file depending on char_func passed """
    def file_conversion(self, in_file, out_file, char_func):
        with open(in_file, 'r') as f_in:
            with open(out_file, 'w') as f_out:
                for line in f_in:
                    wr_line = ""
                    for char in line:
                        wr_line += char_func(char)
                    f_out.write(wr_line)

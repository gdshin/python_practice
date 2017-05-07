
"""
This file does the translation and untranslation of files.
"""

import char_translator
import os.path

class Coder:
    def __init__(self, ts_obj):
        self.obj = ts_obj

    def encode_file(self, in_file, out_file):
        """ empty """
        self.file_conversion(in_file, out_file, self.obj.translate_char)

    def decode_file(self, in_file, out_file):
        """ empty """
        self.file_conversion(in_file, out_file, self.obj.untranslate_char)

    def file_conversion(self, in_file, out_file, char_func):
        try:
            f_in = open(in_file, 'r')
        except:
            raise Exception("Not a valid file: {}".format(in_file))
        f_out = open(out_file, 'w')

        for line in f_in:
            wr_line = ""
            for char in line:
                wr_line += char_func(char)
            f_out.write(wr_line)
        f_in.close()
        f_out.close()


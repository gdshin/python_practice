#! /usr/bin/env python

"""
test_crypto: tests python cryptography code.
"""

import char_translator
import crypto
import sys
from commands import getoutput

usage = "usage: test_crypto filename"

if len(sys.argv) != 2:
    print usage
    sys.exit(1)

input_filename  = sys.argv[1]
output_filename = input_filename + ".encoded"

# Generate a translation string which is a random permutation of
# the letters in the range [a-z].
ts = char_translator.random_permute_chars()

# Create a character translator object.
try:
    ct = char_translator.CharTranslator(ts)
except char_translator.InvalidTranslationString, e:
    print >> sys.stderr, "Invalid translation string created."
    print >> sys.stderr, "Aborting."
    sys.exit(1)

# Encode the file using this object.
crypt = crypto.Coder(ct)
crypt.encode_file(input_filename, output_filename)

# Decode the file using the same translator.
new_input_filename = input_filename + ".new"
crypt.decode_file(output_filename, new_input_filename)

# Test to see if the two files are the same.
output = getoutput("diff -q %s %s" % (input_filename, new_input_filename))

if output:
    print output
    print "Test failed!"
else:
    print "Test passed!"


#!/usr/bin/env python
# coding=utf-8

import re
import codecs
from StringIO import StringIO
import sys

__VERSION__ = "0.0.1"

EXCEPTIONS = [
    # Convert whole words or parts of the words that are exceptions to the
    # diphtong, and one-to-one rules below.
]

DIPHTONGS = [ 
    (u'Lj', u'Љ'),
    (u'Nj', u'Њ'),
    (u'Dž', u'Џ'),
    (u'lj', u'љ'),
    (u'nj', u'њ'),
    (u'dž', u'џ'),
]

PAIRS = [
    (u'A', u'А'), 
    (u'B', u'Б'),
    (u'V', u'В'),
    (u'G', u'Г'),
    (u'D', u'Д'),
    (u'Đ', u'Ђ'),
    (u'E', u'Е'),
    (u'Ž', u'Ж'),
    (u'Z', u'Z'),
    (u'I', u'И'),
    (u'J', u'Ј'),
    (u'K', u'К'),
    (u'L', u'Л'),
    (u'M', u'М'),
    (u'N', u'Н'),
    (u'O', u'О'),
    (u'P', u'П'),
    (u'R', u'Р'),
    (u'S', u'С'),
    (u'T', u'Т'),
    (u'Ć', u'Ћ'),
    (u'U', u'У'),
    (u'F', u'Ф'),
    (u'H', u'Х'),
    (u'C', u'Ц'),
    (u'Č', u'Ч'),
    (u'Š', u'Ш'),
    (u'a', u'а'),
    (u'b', u'б'),
    (u'v', u'в'),
    (u'g', u'г'),
    (u'd', u'д'),
    (u'đ', u'ђ'),
    (u'e', u'е'),
    (u'ž', u'ж'),
    (u'z', u'з'),
    (u'i', u'и'),
    (u'j', u'ј'),
    (u'k', u'к'),
    (u'l', u'л'),
    (u'm', u'м'),
    (u'n', u'н'),
    (u'o', u'о'),
    (u'p', u'п'),
    (u'r', u'р'),
    (u's', u'с'),
    (u't', u'т'),
    (u'ć', u'ћ'),
    (u'u', u'у'),
    (u'f', u'ф'),
    (u'h', u'х'),
    (u'c', u'ц'),
    (u'č', u'ч'),
    (u'š', u'ш'),
    ]

def transliterate(str, transpairs):
    """Transliterate str based on transpairs pairs of strings
    
    `str` is a unicode string to be parsed.
    `transpairs` is a list of 2-tuples containing character pairs

    There is no need to prepend `(?u)` to the first character in a character
    pair, as this is done for you by `transliterate()`.

    """

    for pair in transpairs:
        sourcechar = u'(?u)' + pair[0]
        regexp = re.compile(sourcechar, re.UNICODE)
        str = regexp.sub(pair[1], str)
    return str

def printerror(error, code="Unknown"):
        print """
**************************************************************
ERROR (%s)
**************************************************************
%s
**************************************************************
""" % (code, error)


def printdocs(version=__VERSION__):
    print """
%s
==============================================================

lat2cyr.py %s

==============================================================

OVERVIEW
--------------------------------------------------------------
This script will take one or more UTF-8 encoded files, and 
transliterate all Serbian Latin characters in those files to 
matching Cyrillic characters.

USAGE
--------------------------------------------------------------
To use this script, supply the name(s) of the file(s) to 
transliterate. The transliterated text will be printed out on 
stdout. If you want to save the results, we suggest you pipe 
the output into a file.

If multiple files are passed to this script, the results will
be concatenated!

EXAMPLE
--------------------------------------------------------------
$ python lat2cyr.py mytextfile.txt

==============================================================
""" % (version)


def main():
    try:
        arguments = sys.argv[1:] 
    except IndexError:
        printdocs()
        quit()
    for argument in arguments:
        cloaca = StringIO()
        for argument in arguments:
            try:
                infile = codecs.open(argument, 'r', 'utf-8')
            except IOError:
                printerror(error="""File `%s` does not exist or is not readable.
Please specify a valid file.""" % argument, code=2)
                quit(2)
            current = infile.read()
            infile.close()
            for pairs in [EXCEPTIONS, DIPHTONGS, PAIRS]:
                current = transliterate(current, pairs)
                cloaca.write(current)
        print cloaca.getvalue().encode("utf-8")
        cloaca.close()

if __name__ == "__main__":
    main()


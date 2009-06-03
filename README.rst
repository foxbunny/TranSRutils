===========
TranSRutils
===========

Overview
--------

TranSRutils is a set of utilities to aid Serbian language translators.
Currently it contains transliteration utilities for Cyrillic-to-Latin and
Latin-to-Cyrillic conversion of UTF-8 text documents, and I hope the tool set
will grow if there is need for more tools.

Implementation
--------------

TranSRutils are written in Python_, and they should be portable to many
platforms including Microsoft Windows, and Mac OSX. However, I use Linux
exclusively, so I haven't tested the tools under other systems. Please report
any bugs you find to bg (dot) branko (at) gmail (dot) com

.. _Python: http://www.python.org/

cyr2lat.py and lat2cyr.py
-------------------------

``cyr2lat.py`` and ``lat2cyr.py`` are transliteration tools. They are written
like basic UNIX utilities, which means they only display the results on the
screen. They are meant to be connected to other utilities using pipes.

On a UNIX-like system, you will use these scripts like this::

    $ cyr2lat.py my_text_file.txt > my_latin_text_file.txt
    $ lat2cyr.py my_text_file.txt > my_cyrillic_text_file.txt

Transliteration tables
~~~~~~~~~~~~~~~~~~~~~~

Both ``cyr2lat.py`` and ``lat2cyr.py`` contain transliteration tables. The
tables define transliteration pairs consisting of unicode regexp and a string.
Unicode regexp is used to find text in the files, and the string is used to
replace the matched text.

Use of regexp as the first part of the pair gives us flexibility in handling
exceptions, which is especially important for Latin to Cyrillic conversion.

I have made room for such expression, but I currently do not have time to
research. I will most probably add them as I stumble on them. If you can find
any resources on exceptions, I would appreciate it if you could send me a
link.

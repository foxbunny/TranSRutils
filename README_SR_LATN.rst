===========
TranSRutils
===========

Uvod
----

TranSRutils je zbirka alata za prevodioce srpskog jezika. Trenutno sadrži
alate za transliteraciju teksta iz ćirilice u latinicu i obratno, a nadam se
da će, ukoliko postoji potreba, kolekcija alata postati sveobuhvatnija.

Implementacija
--------------

TranSRutils su pisani u Python_-u pa su samim tim prenosivi na različite
platforme, uključujući i Windows i Mac OSX. Međutim, ja lično koristim samo
Linux, pa softver testiram samo na toj platformi. Sve pronađene bagove
prijavite na adresu bg (tačka) branko (majmun) gmail (tačka) com

_ Python: http://www.python.org/

cyr2lat.py i lat2cyr.py
-----------------------

``cyr2lat.py`` i ``lat2cyr.py`` su alati za transliteraciju. Oni su napisani
kao klasični UNIX alati, što znači da se rezultati transliteracije ispisuju na
ekranu i ne upisuju u fajlove. Зamišljeni su da rade u tandemu sa drugim
alatima upotrebom pajpova.

Na UNIX-olikim sistemima, ove alate ćete koristiti ovako:

    $ cyr2lat.py my_text_file.txt > my_latin_text_file.txt
    $ lat2cyr.py my_text_file.txt > my_cyrillic_text_file.txt

Tabele za transliteraciju
~~~~~~~~~~~~~~~~~~~~~~~~~

I ``cyr2lat.py`` i ``lat2cyr.py`` sadrže tabele za transliteraciju. Te tabele
određuju parove za transliteraciju koji se sastoje od unicode pravilnog izraza
i stringa. Pravilni izraz služi za pronalaženje teksta u fajlovima dok se
string koristi kao zamena za pronađeni tekst.

Korišćenje pravilnih izraza kao prvog dela parova daje fleksibilnost u radu sa
izuzecima, što je naročito važno u tranliteraciji latiničnog teksta u 
ćirilični.

Зa izuzetke je ostavljen prostor, ali trenutno nemam vremena za proučavanje tog
problema. Verovatno ću ih dodavati kako budem nailazio na njih. Ako pronađete
izvore koji se bave ovom temom, pošaljite mi link.

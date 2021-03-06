===========
TranSRutils
===========

Увод
----

TranSRutils је збирка алата за преводиоце српског језика. Тренутно садржи
алате за транслитерацију текста из ћирилице у латиницу и обратно, а надам се
да ће, уколико постоји потреба, колекција алата постати свеобухватнија.

Имплементација
--------------

TranSRutils су писани у Python_-у па су самим тим преносиви на различите
платформе, укључујући и Windows i Mac OSX. Међутим, ја лично користим само
Linux, па софтвер тестирам само на тој платформи. Све пронађене багове
пријавите на адресу bg (тачка) branko (мајмун) gmail (тачка) com

.. _Python: http://www.python.org/

cyr2lat.py и lat2cyr.py
-----------------------

``cyr2lat.py`` и ``lat2cyr.py`` су алати за транслитерацију. Они су написани
као класични UNIX алати, што значи да се резултати транслитерације исписују на
екрану и не уписују у фајлове. Замишљени су да раде у тандему са другим
алатима употребом пајпова.

На UNIX-оликим системима, ове алате ћете користити овако:

    $ cyr2lat.py my_text_file.txt > my_latin_text_file.txt
    $ lat2cyr.py my_text_file.txt > my_cyrillic_text_file.txt

Табеле за транслитерацију
~~~~~~~~~~~~~~~~~~~~~~~~~

И ``cyr2lat.py`` и ``lat2cyr.py`` садрже табеле за транслитерацију. Те табеле
одређују парове за транслитерацију који се састоје од unicode правилног израза
и стринга. Правилни израз служи за проналажење текста у фајловима док се
стринг користи као замена за пронађени текст.

Коришћење правилних израза као првог дела парова даје флексибилност у раду са
изузецима, што је нарочито важно у транлитерацији латиничног текста у
ћирилични.

За изузетке је остављен простор, али тренутно немам времена за проучавање тог
проблема. Вероватно ћу их додавати како будем наилазио на њих. Ако пронађете
изворе који се баве овом темом, пошаљите ми линк.

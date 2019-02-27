# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# Um die Daten in einer Datenbank zu speicher muessen wir das ausgegebene Dictionary in einen COntainer Item umwandeln. Das geschieht mit Hilfe der items.py

import scrapy

# Container fuer unseren Output
class MeinscrapyItem(scrapy.Item):
    # define the fields for your item here like:

    # Hier wandeln wir die Dictionaries in Container um
    aktuelle_temperaturen = scrapy.Field()
    minimale_temperatur = scrapy.Field()
    # pass muss auskommentiert werden, da sonst die Definitionen nicht greifen

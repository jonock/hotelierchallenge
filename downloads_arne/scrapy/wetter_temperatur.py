# Import von Scrapy
import scrapy

# Erstellen einer Klasse, die aus Scrapy vereerbt wird
class WetterSpider (scrapy.Spider):
    # Name fuer die Spider vergeben (die Variable muss zwingend name heissen). Diesen Namen rufen wir ueber die Command Prompt auf. Bspw. scrapy crawl wetter
    name = "wettertemperatur"
    # Liste mit den Webseiten, die wir Crawlen wollen (muss zwingend start_url heissen)
    start_urls = [
        'https://www.meteoblue.com/de/wetter/vorhersage/woche/st.-gallen_schweiz_2658822'
    ]

    # Erstellen der Methode parse (Varibale response wird den Sourcecode der Internetseite erhalten, die wir Crawlen wollen)
    def parse (self, response):

        # Erstellen einer Variable fuer die Temperatur. Response gibt eine Liste zurueck
        # Ausgabe mit CSS Selektor
        aktuelle_temperaturen = response.css(".tab_temp_max::text").extract(),
        # Ausgabe mit xpath Selektor
        minimale_temperatur = response.xpath("//div[@class='tab_temp_max']/text()").extract()

        # Return/Yield statement (gibt immer ein dictiornary zuruck)
        yield {
            # dictiornary erfordert immer Key and Value
            'aktuelle_temperaturen' : aktuelle_temperaturen,
            'minimale_temperatur' : minimale_temperatur
        }

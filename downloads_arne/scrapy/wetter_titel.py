# Import von Scrapy
import scrapy

# Erstellen einer Klasse, die aus Scrapy vereerbt wird
class WetterSpider (scrapy.Spider):
    # Name fuer die Spider vergeben (die Variable muss zwingend name heissen). Diesen Namen rufen wir ueber die Command Prompt auf. Bspw. scrapy crawl wetter
    name = "wettertitel"
    # Liste mit den Webseiten, die wir Crawlen wollen (muss zwingend start_url heissen)
    start_urls = [
        'https://www.meteoblue.com/de/wetter/vorhersage/woche/st.-gallen_schweiz_2658822'
    ]

    # Erstellen der Methode parse. Wird durch Scrapy vorgegeben. (Varibale response wird den Sourcecode der Internetseite erhalten, die wir Crawlen wollen)
    def parse (self, response):

        # Erstellen einer Variable fuer den Titel der Webseite. Response gibt eine Liste zurueck. Den Namen der Variable bekommen wir ueber die Webseite im Browser
        # Ausgabe mit CSS Selektor
        titel = response.css("title::text").extract()

        # Return/Yield statement (gibt immer ein dictiornary zuruck)
        yield {
        'titel' : titel
        }

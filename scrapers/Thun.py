import scrapy


class QuotesSpider(scrapy.Spider):
    name = "thun"
    start_urls = [
        'https://fcthun.ch/de/Teams/Profis/Team/Kader',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'tags': quote.css('div.name p.::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

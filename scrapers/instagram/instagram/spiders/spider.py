import scrapy


class HashtagSpider(scrapy.Spider):
    name = "instahashtags"

    def start_requests(self):
        urls = [
            'https://www.instagram.com/explore/tags/berlin/',
            'https://www.instagram.com/explore/tags/basel/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

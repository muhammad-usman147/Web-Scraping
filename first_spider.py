import scrapy
class SpiderQuotes(scrapy.Spider):
    name='usman-quote'
    start_urls=[
        'http://quotes.toscrape.com'
    ]

    def parse(self,response):
        all_div=response.css('div.quote')
        for all_div in all_div:

            bod=all_div.css('span.text::text').extract()
            tit=all_div.css('.tag::text').extract()
            author= all_div.css('.author::text').extract()
            yield {'body':bod,'tags':tit,'author':author}
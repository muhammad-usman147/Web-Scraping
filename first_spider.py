import scrapy
from ..items import FirstspiderItem
class SpiderCrawler(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]
    def parse(self,response):
        all_div_quotes=response.css('div.quote')
        item=FirstspiderItem()
        for all_div_quotes in all_div_quotes:

            title=all_div_quotes.css('span.text::text').extract()
            author=all_div_quotes.css('.author::text').extract()
            tags=all_div_quotes.css('.tag::text').extract()
            item['item_title']=title
            item['item_author']=author
            item['item_tags']=tags
            yield item
import scrapy

class ScrapingSpider(scrapy.Spider):
    name='linkstoscrape'
    link=1
    start_urls=[
        'http://quotes.toscrape.com/page/1/'
    ]
    def parse(self,response):
        all_div_items=response.css("div.quote")
        for all_div_items in all_div_items:
            text=all_div_items.css("span.text::text").extract()
            author=all_div_items.css("span.author::text").extract()
            tags=all_div_items.css("a.tag::text").extract()
            dic={'text':text,'author':author,'tags':tags,'page':self.link}
            yield dic
        next_page='http://quotes.toscrape.com/page/'+str(ScrapingSpider.link)+'/'
        if ScrapingSpider.link <11:
            ScrapingSpider.link+=1
            yield response.follow(next_page,callback=self.parse)

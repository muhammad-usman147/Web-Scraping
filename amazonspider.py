# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspidy'
    #allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?k=books+best+sellers&crid=WP6O01PC4830&sprefix=books%2Caps%2C1130&ref=nb_sb_ss_i_1_5'
    ]
    page=2
    def parse(self, response):
        
        book_author=response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        book_name=response.css('.a-color-base.a-text-normal').css('::text').extract()
        book_price=response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        name=[]
        author=[]
        price=[]
        for x,y in zip(book_name,book_author):
            name.append(x.strip())
            author.append(y.strip())
        for p in book_price:
            if p !='.':
                price.append(p)
        dic={
            'cover':name,
            'author':author,
            'price':price,
            'lenth1':[len(name),len(author),len(price)]
            }
        yield dic
        next_page='https://www.amazon.com/s?k=books+best+sellers&page='+str(self.page)+'&crid=366VCTHNK1PND&qid=1559691401&sprefix=books%2Caps%2C332&ref=sr_pg_2'
        if self.page <=10:
            self.page+=1
            yield response.follow(next_page,callback=self.parse)
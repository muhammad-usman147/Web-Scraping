import scrapy
from scrapy.http import FormRequest

class LoginToScrape(scrapy.Spider):
    name='loginspider'
    link=1
    password='pakola123'
    start_urls=[

        'http://quotes.toscrape.com/login'
    ]
    def parse(self,response):
      
        token=response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'ushakeel909@hotmail.com',
            'password':self.password
        },callback=self.SpiderParser)
    def SpiderParser(self,response):
        get_div=response.css('div.quote')
        for spidy in get_div:
            title=spidy.css("span.text::text").extract()
            author=spidy.css(".author::text").extract()
            tags=spidy.css(".tag::text").extract()
            dic={
                'text':title, 'author':author, 'tags':tags
            }
            yield dic
            with open('spider.txt','a') as f:
                f.write('\n {} \n'.format(dic))
        next_page='http://quotes.toscrape.com/page/'+str(+self.link)+'/'
        if self.link <=10:
            self.link+=1
            
            yield response.follow(next_page,callback=self.SpiderParser)
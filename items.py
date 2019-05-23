# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#item clears the data of the dictionary in the readable format
class FirstspiderItem(scrapy.Item):
    # define the fields for your item here like:
    item_title=scrapy.Field()
    item_author=scrapy.Field()
    item_tags=scrapy.Field()
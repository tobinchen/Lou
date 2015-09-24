# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    lou = scrapy.Field()
    square = scrapy.Field()
    number = scrapy.Field()
    amount = scrapy.Field()
    price = scrapy.Field()
    pass

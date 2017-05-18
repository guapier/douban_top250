# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name=scrapy.Field()
    #en_author=scrapy.Field()
    #cn_author=scrapy.Field()
    #publishment=scrapy.Field()
    #book_price=scrapy.Field()
    #publish_time=scrapy.Field()
    book_info=scrapy.Field()
    book_desc=scrapy.Field()
    book_rate=scrapy.Field()
    book_url=scrapy.Field()
    book_comments=scrapy.Field()

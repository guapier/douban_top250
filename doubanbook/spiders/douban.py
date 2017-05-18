# -*- coding: utf-8 -*-
import scrapy
from doubanbook.items import DoubanbookItem
from scrapy import Request
import logging

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = ['http://book.douban.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://book.douban.com/top250'
        yield Request(url, headers=self.headers)


    def parse(self, response):
        for item in response.css('div.article div.indent table'):
            book=DoubanbookItem()
            book_name=item.css('tr.item td div.pl2 a::text').extract_first()
            book_url=item.css('tr.item td div.pl2 a::attr(href)').extract_first()
            book_info=item.css('tr.item td p.pl::text').extract_first()
            book_rate=item.css('span.rating_nums::text').extract_first()
            book_comments=item.css('span.pl::text').extract_first()
            book_desc=item.css('span.inq::text').extract_first()
            self.logger.info('Parse function called on %s', response.url)
            self.logger.info('book_name\'s value is  %s', response.url)

            book['book_name']=book_name
            book['book_url']=book_url
            book['book_info']=book_info
            book['book_rate']=book_rate
            book['book_desc']=book_desc
            book['book_comments']=book_comments
            yield book


        next_page = response.css('span.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

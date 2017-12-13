# -*- coding: utf-8 -*-
import scrapy
from quotes.items import QuotesItem
from scrapy.http import Request
class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    #allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self, response):
        quote_sel= response.xpath('//div[@class="quote"]')
        for sel in quote_sel:
            #print i
            quote = sel.xpath('span[@class="text"]/text()').extract_first()
            #print quote
            author = sel.xpath('span/small[@class="author"]/text()').extract_first()
            #print author
            item =  QuotesItem(
                quote = quote,
                author = author)
            yield item
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        next = response.urljoin(next_url)
        #print next
        if next_url:
            yield Request(url= next)




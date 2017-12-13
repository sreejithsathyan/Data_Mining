# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import FormRequest
import json
from wordpress.items import WordpressItem

class WordpressSpiderSpider(scrapy.Spider):
    name = 'wordpress_spider'
    allowed_domains = ['pythonhelp.wordpress.com']
    start_urls = ['http://pythonhelp.wordpress.com/']
    
    flag = True
    page = 0

    def parse(self, response):
        if self.flag:
            sel = Selector(text=response.body)
            self.flag = False
            pass
        else:
            d = json.loads(response.body)
            data = d.get('html')
            sel = Selector(text=data)
        #print '2222222222222222222222222222222222222222222222',sel
        if sel:
	        titles =  sel.xpath('//h1[@class="entry-title"]/a/text()').extract()
	        for title in titles:
	        	#print title
	        	item = WordpressItem(title = title)

	        	yield item
	        self.page = self.page+1
	        #print self.page
	        url = 'https://pythonhelp.wordpress.com/?infinity=scrolling'
	        formdata={'action':'infinite_scroll',
	                  'page':str(self.page),
	                  'order':'DESC',
	                  'last_post_date':'2016-04-24 17:38:39',}
	        yield FormRequest(url=url, callback=self.parse, formdata=formdata)
	           

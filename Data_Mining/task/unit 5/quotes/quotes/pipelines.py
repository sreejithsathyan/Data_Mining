# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QuotesPipeline(object):
    def process_item(self, item, spider):
        
        file_name = item.get("author").replace(' ','_')+'.jl'  
        #print file_name
        f = open(file_name,"a")
        quote = item.get("quote").encode("utf-8")
        quote = quote.replace('”','')
        quote = quote.replace('“','')
        #print quote
        f.write(quote +"\n")
        f.close()

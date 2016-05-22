# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class SearchPipeline(object):
    def process_item(self, item, spider):
        if item['search_num']<>0:
            return item
        else:
            raise DropItem("There is no result from %s" % item)

import json

class JsonWritePipeline(object):
    def __init__(self):
        self.file=open('items.txt','wb')

    def process_item(self,item,spider):
        line=json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item

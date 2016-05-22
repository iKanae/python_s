# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# define the fields for your item here like:
#  name = scrapy.Field()


import scrapy

class SearchItem(scrapy.Item):
    search_num=scrapy.Field()
    search_result=scrapy.Field()
    search_package=scrapy.Field()

class QuestionItem(scrapy.Item):
    title=scrapy.Field()
    url=scrapy.Field()
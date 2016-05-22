# -*- coding:utf-8 -*-
import scrapy
from tutorial.items import QuestionItem
import re
from scrapy.http import Request,FormRequest
from scrapy.contrib.spiders import CrawlSpider, Rule
from tutorial.settings import *
# -*- coding:utf-8 -*-
class ZhihuSpider(scrapy.Spider):
    name="zhihu"
    allowd_domains=["zhihu.com"]
    start_urls=["https://www.zhihu.com/"]

    def start_requests(self):
        for i,url in enumerate(self.start_urls):
            yield Request(url,meta={"cookiejar":1},
                              cookies=COOKIES,
                              callback=self.parse_item)

    def parse_item(self,response):
        item=QuestionItem()
        item["title"]=response.xpath('//a[@class="question_link"]/text()').extract()
        item["url"]=response.xpath('//a[@class="question_link"]/@href').extract()
        yield item

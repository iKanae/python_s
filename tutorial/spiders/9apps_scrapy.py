import scrapy
from tutorial.items import SearchItem
from tutorial.self_function import create_urls
import re

class DoubanSpider(scrapy.Spider):
    name="9apps"
    keyword=["IPL","Piano","hike","hello"]
    start_urls=create_urls(keyword)
    
    def parse(self,response):
        item=SearchItem()
        item['search_num']=response.xpath('//span[@style="color:red;"]/text()').extract()
        item['search_result']=response.xpath("//span[@class='name']/text()").extract()
        packageurls=response.xpath('//a[@rel="nofollow"]/@href').extract()
        item['search_package']=map(lambda x : re.findall(r'down/(.*)/app',x),packageurls)
        yield item


#list=["a3aa","ooa2ass","/jump/down/com.qihoo.security/app/?f=12_0_3_0_1"]
#print map(lambda x : re.findall(r"down/(.*)/app",x),list)
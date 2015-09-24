# -*- coding: utf-8 -*-
# __author__ = 'tobinchen'


import scrapy
from LouSpider.items import LouspiderItem
from scrapy.http import FormRequest
from scrapy.selector import Selector

class lou(scrapy.spiders.Spider):
    name = "lou"
    #allowed_domains = ["www.qyfgj.cn"]
    start_urls = [
        "http://www.qyfgj.cn/gz/",
    ]

    def parse(self,response):
        for n in range(2006,2016):
            for y in range(1,13):
                formdata={'nian': str(n), 'yue1': str(y),'yue2':str(y),'tijiao':'统 计'}
                yield FormRequest(url = 'http://www.qyfgj.cn/gz/ti_result.asp',
formdata = formdata,callback=self.parseData)

    def parseData(self, response):
        sel = Selector(response)

        trs=sel.xpath("//table[@width=580]/tr")
        del trs[0]
        for tr in trs:
            qyItem=LouspiderItem()
            qyItem['name']=tr.extract()
            yield  qyItem
            #items.append(qyItem)
        #return  items
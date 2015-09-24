# -*- coding: utf-8 -*-
# __author__ = 'tobinchen'

import sys
#reload(sys)
#sys.setdefaultencoding("gb2312")

from datetime import datetime
import scrapy
from LouSpider.items import LouspiderItem
from scrapy.http import FormRequest
from scrapy.selector import Selector
from scrapy import log

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
                req= FormRequest(url = 'http://www.qyfgj.cn/gz/ti_result.asp',
formdata = formdata,callback=self.parseData)
                req.meta['date']=datetime(n,y,1)
                yield req

    def parseData(self, response):
        sel = Selector(response)

        trs=sel.xpath("//table[@width=580]/tr")
        if len(trs)<1:
            return

        del trs[0]
        for tr in trs:
            tds=tr.xpath(".//td/text()").extract()
            qyItem=LouspiderItem()
            qyItem['date']=response.meta['date']
            qyItem['lou']=tds[0]
            qyItem['square']=tds[1]
            qyItem['number']=tds[2]
            qyItem['amount']=tds[3]
            qyItem['price']=tds[4]

            print qyItem['lou'],tds[0]
            yield  qyItem
            #items.append(qyItem)
        #return  items
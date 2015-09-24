# -*- coding: utf-8 -*-
# __author__ = 'tobinchen'

from scrapy.http import Request
from scrapy.exceptions import NotConfigured

class LookMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('REFERER_ENABLED'):
            raise NotConfigured
        return cls()

    def process_spider_output(self, response, result, spider):
        def _set_referer(r):
            if isinstance(r, Request):
                r.headers.setdefault('Referer', response.url)
            return r
        print 'result:',result
        return result
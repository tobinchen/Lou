# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs

class LouspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('output.txt', 'a+', 'utf-8')
    def process_item(self, item, spider):
        record=[ item['date'].strftime('%Y-%m-%d'),item['lou'],item['square'],item['number'],item['amount'],item['price']]
        lines=','.join(record)
        self.file.write(lines+'\n')
        return item

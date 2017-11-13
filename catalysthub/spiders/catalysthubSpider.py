#!/usr/bin/python                                                                                                           
#-*- encoding:utf-8 -*-
import scrapy
import logging
import json
from catalysthub.items import cataItem
import datetime
import re
import sys
reload(sys)

class CatalysthubSpider(scrapy.Spider):
    name = "catalysthubSpider"
    base_url = 'http://www.catalysthub.net'
    start_urls = []

    def __init__(self):
        sys.setdefaultencoding('utf8') 
        for i in range(1):
            url = self.base_url+'/?p='+str(i)
            self.start_urls.append(url)
   
    def parse(self,response):
        try:
            item = cataItem()
            #获取数据区域
            zone = response.xpath('//table[@class="table table-hover"]/tr')
            for td in zone:
                td_text = td.xpath('./td/text()').extract()
                item['space_group'] = td_text[0]
                item['hm'] = td_text[1]
                item['hall'] = td_text[2]
                item['lattice_system'] = td_text[3]
                item['band_gap'] = td_text[4]
                item['source'] = td_text[6]
                td_a_text = td.xpath('./td/a/text()').extract()
                item['full_formula'] = td_a_text[0] 
                item['structure_file'] = td_a_text[1] + '|' + td_a_text[2]
                print(item)
                yield item
        except Exception as e:  # not available site
            logging.error(e, exc_info=True)
            logging.error("Error process:"+response.url)


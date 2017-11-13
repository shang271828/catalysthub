# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class cataItem(scrapy.Item):
    # define the fields for your item here like:
    space_group = scrapy.Field()
    hm = scrapy.Field()
    hall = scrapy.Field()
    lattice_system = scrapy.Field()
    band_gap = scrapy.Field()
    source = scrapy.Field()
    full_formula = scrapy.Field()
    structure_file = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    pass


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Movieurl = scrapy.Field()
    Moviename = scrapy.Field()
    Moviecategory = scrapy.Field()
    actors = scrapy.Field()
    Introductions = scrapy.Field()
    Image = scrapy.Field()
    Downloadurl = scrapy.Field()


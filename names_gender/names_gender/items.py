# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NamesGenderItem(scrapy.Item):
    name = scrapy.Field()
    gender = scrapy.Field()

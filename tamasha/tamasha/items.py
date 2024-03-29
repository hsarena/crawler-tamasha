# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TamashaItem(Item):
    category = Field()
    title = Field()
    link = Field()
    date_added = Field()
    publisher = Field()
    publisher_logo = Field()
    description = Field()
    tags = Field()
    thumbnail = Field()
    url = Field()
    qr = Field()
    embed = Field()
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy


class ArticlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name: str | None = None
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    body = scrapy.Field()
    tag = scrapy.Field()
    


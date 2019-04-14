# -*- coding: utf-8 -*-
import scrapy
import re
from tamasha.items import TamashaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class VideosSpider(CrawlSpider):
    name = 'videos-link'
    allowed_domains = ['tamasha.com']


    start_urls = ['https://tamasha.com/']
    rules = (Rule(LinkExtractor('https://tamasha.com/v/'), callback='parse_item', follow=True),)

    def parse_item(self, response):

        item = TamashaItem()
        item['category'] = response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/a/text()').get()
        item['title'] = response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h1/text()').get()
        item['link'] = response.url
        item['publisher'] = response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/a[2]/text()').get()
        item['publisher_logo'] = response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/a[1]/img/@src').get()
        tmp = str(response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[3]/div[1]/span[2]').get())
        item['date_added'] = re.sub('<[^<]+?>', '', tmp)
        item['description'] = str(response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[3]/div[1]').get())
        tags = response.xpath('//*[@id="pageContent"]/div/div/div[1]/div[2]/div[2]/div[3]/ul/li')
        tag = []
        for t in tags:
            tag.append(str(t.xpath('a/text()').get()))
        item['tags'] = ' , '.join(tag)
        item['thumbnail'] = response.xpath('// *[ @ id = "pageContent"] / div / div / div[1] / div[2] / div[1] / div / div/*/@poster').get()
        print(item)
        return item
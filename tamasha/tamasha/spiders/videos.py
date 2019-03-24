# -*- coding: utf-8 -*-
import scrapy
from tamasha.items import TamashaItem

class VideosSpider(scrapy.Spider):
    name = 'videos'
    allowed_domains = ['tamasha.com']
    categories = ['entertainment', 'sport', 'tech'
                  'animation', 'education', 'movie',
                  'news', 'music', 'game',
                  'tourism', 'comedy', 'religious',
                  'economics', 'cooking', 'social',
                  'kids', 'science', 'motherhood',
                  'documentary', 'culture', 'health',
                  '360', 'misc']

    start_urls = ['https://tamasha.com/{0}'.format(category) for category in categories]
    custom_settings = {
        'DEPTH_LIMIT': '1',
    }

    def parse(self, response):
        items = []
        category = response.xpath('//*[@id="pageContent"]/div/div[1]/div/div[1]/h1/text()').get()
        videos = response.xpath('///*[@id="pageContent"]/div/div[2]/div[1]/div[2]/div/div')
        for video in videos:
            item = TamashaItem()
            item['category'] = category
            item['title'] = video.xpath('div/a/@title').get()
            item['link'] = video.xpath('div/a/@href').get()
            items.append(item)
        #print(items)
        return items

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZqiCompanyItem(scrapy.Item):
    city_name = scrapy.Field()
    city_url = scrapy.Field()


class CompanyMessage(scrapy.Item):
    collection = table = 'zhongqi'
    company_name = scrapy.Field()
    company_mes = scrapy.Field()


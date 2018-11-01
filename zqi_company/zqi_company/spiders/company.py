# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
from lxml import etree
from zqi_company.items import ZqiCompanyItem,CompanyMessage

n = 1





class CompanySpider(scrapy.Spider):

    name = 'company'
    allowed_domains = ['85781.com']
    start_urls = ['http://www.85781.com/']

    def start_requests(self):
        start_urls='http://85781.com/'
        yield Request(url=start_urls, callback=self.get_city)


    def get_city(self,response):

        html= etree.HTML(response.text)
        citys_name=html.xpath('//div[@id="letterlist"]//dd')
        for one_city in citys_name:
            item=ZqiCompanyItem()
            item["city_name"] = one_city.xpath('.//text()')[0]
            new_url = one_city.xpath('.//@href')[0]

            item["city_url"]='www.85781.com'+new_url
            yield item
        city_links = html.xpath('//div[@id="letterlist"]//dd//@href')
        # print('*' * 60)
        # print(city_links)
        for one_link in city_links:
            url = 'http://www.85781.com'+one_link
            yield Request(url=url, meta={'urls': url}, callback=self.get_message)
    #


    def get_message(self,response):
        global n
        urls = response.meta['urls']
        html = etree.HTML(response.text)
        company_message = html.xpath('//div[contains(@class,"container")]//ul[contains(@class,"list")]//li')
        for one_message in company_message:
            item1=CompanyMessage()
            item1["company_name"] = one_message.xpath('./a/text()')[0]
            item1["company_mes"] = one_message.xpath('./text()')[1]
            print('*' * 30)
            print('打开item1')
            print('正在下载第%d条数据' % n)
            n += 1
            yield item1

        page_as = html.xpath('//*[@id="pageLink"]/a')
        if len(page_as):
            page_urls = html.xpath('//*[@id="pageLink"]/a/@href')
            page_url=page_urls[-1]
            num = page_url.split('_')[1]
            page_num = num.split('.')[0]

                # http: // www.85781.com / sichuan / deyang / index_2.html
            for page in range(2,int(page_num)+1):
                page_link=urls+'index_'+str(page)+'.html'
                # print('*' * 60)
                # print(page_link)
                yield Request(url=page_link, callback=self.all_page)


    def all_page(self,response):
        global n
        html = etree.HTML(response.text)
        company_message = html.xpath('//div[contains(@class,"container")]//ul[contains(@class,"list")]//li')
        for one_message in company_message:
            item2 = CompanyMessage()
            item2["company_name"] = one_message.xpath('./a/text()')[0]
            item2["company_mes"] = one_message.xpath('./text()')[1]
            print('*' * 30)
            print('打开item2')
            print('正在下载第%d条数据' % n)
            n += 1
            yield item2















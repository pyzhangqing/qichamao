# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

class ZqiCompanyPipeline(object):
    def process_item(self, item, spider):
        return item



class MysqlPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.num2 = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        print('打开mysql')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()
        print('关闭mysql')

    def process_item(self, item, spider):
        self.num2 += 1
        if item:
            company_mes = item["company_mes"]
            company_name = item["company_name"]
            sql = "insert into zhongqi_company (company_name,company_mes) values ('%s','%s')" % (company_name, company_mes)
            print('*'*20)
            print(sql)
            self.cursor.execute(sql)
            self.db.commit()
            print('第%d个name存储到mysql成功' % self.num2)

            return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        manhua = item.collection
        self.db[manhua].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
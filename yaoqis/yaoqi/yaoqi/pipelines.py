# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import pymongo
from .modles import Yaoqis


class YaoqiPipeline(object):
    def process_item(self, item, spider):
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


class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['cover'])


#SQLAlchemy

class MySqlPipeline(object):
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/movie?charset=utf8", max_overflow=5)
        print("----------*******************")
        print(self.engine)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = None

    def open_spider(self, spider):
        self.session = self.session_maker()

    def process_item(self, item, spider):
        yaoqis = Yaoqis()
        yaoqis.title = item['title']
        yaoqis.cover = item['cover']

        self.session.add(yaoqis)
        self.session.commit()

        return item

    def close_spider(self, spider):
        self.session.close()


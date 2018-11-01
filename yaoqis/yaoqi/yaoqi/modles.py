from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/movie?charset=utf8", max_overflow=5,encoding='utf-8')
Base = declarative_base()

class Yaoqis(Base):
    __tablename__ = 'yaoqis'
    id = Column(Integer, primary_key=True, autoincrement=True)    #主键，自增
    title = Column(String(512))
    cover = Column(String(1024))

    def __repr__(self):
        output = "(%d,%s)" % (self.id, self.title)
        return output

Base.metadata.create_all(engine)
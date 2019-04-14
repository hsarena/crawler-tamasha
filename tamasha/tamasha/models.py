from sqlalchemy import create_engine, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings
import pymysql


DeclarativeBase = declarative_base()

def db_connect():

    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class TamashaDB(DeclarativeBase):
    __tablename__ = "tamasha"
    #__table_args__ = tuple(UniqueConstraint('title', 'link', name='my_2uniq'))

    id = Column(Integer, primary_key=True)
    category = Column('category', String(100))
    title = Column('title', String(250), unique=True)
    link = Column('link', String(100))
    date_added = Column('date_added', String(100))
    publisher = Column('publisher', String(50))
    publisher_logo = Column('publisher', String(70))
    tags = Column('tags', String(30))
    description = Column('description', Text())
    thumbnail = Column('thumbnail', String(70))



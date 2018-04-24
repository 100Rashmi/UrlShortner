from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ShortendUrl(Base):
    __tablename__ = 'shortend_url'
    url_id = Column(Integer, autoincrement=True, primary_key=True)
    status = Column(String(30))
    long_url = Column(String(2500))
    created_time = Column(DateTime)
    short_url = Column(String(10), unique=True)









from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UrlInfo(Base):
    __tablename__ = 'urlinfo'
    url_id = Column(Integer, autoincrement=True, primary_key=True)
    status = Column(String(32))
    long_url = Column(String(2048))
    created_time = Column(DateTime)
    updated_time = Column(DateTime)
    short_url = Column(String(32), unique=True)









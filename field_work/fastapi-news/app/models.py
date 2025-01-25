from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    title = Column(String, index=True)
    body = Column(Text)
    link = Column(String)
    
    category_id = Column(Integer, ForeignKey('categories.id'))
    reporter_id = Column(Integer, ForeignKey('reporters.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    category = relationship("Category")
    reporter = relationship("Reporter")
    publisher = relationship("Publisher")

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)

class Reporter(Base):
    __tablename__ = "reporters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)

class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, nullable=True)
    website = Column(String, nullable=True, unique=True)

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    news_id = Column(Integer, ForeignKey('news.id'))
    url = Column(String)

    news = relationship("News")

    
class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True, index=True)
    news_id = Column(Integer, ForeignKey('news.id'))
    summary_text = Column(Text)
    
    
class SummaryCreate(Base):
    __tablename__ = " summaries"
    id = Column(Integer, primary_key=True, index=True)
    summary_text = Column(Text)
    news_id = Column(Integer, ForeignKey('news.id'))
    news = relationship("News")
    

    
    
    
    
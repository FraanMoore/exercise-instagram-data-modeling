import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String (20), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)
    phone = Column(Integer(8))
    direcction = Column(String(100))
    birthdate = Column(Integer(8), nullable=False)
    follower = relationship('follower')
    comment = relationship('comment')
    post = relationship('post')    

class Comment(Base):
    __tablename__= 'comment'
    id = Column (Integer, primary_key=True)
    comment_text = Column(String (300))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey ('post.id'))
   
class Post(Base):
    __tablename__= 'post'
    id = Column (Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('comment')
    media = relationship('media')

class Follower(Base):
    __tablename__= 'follower'
    id = Column(String, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    
class Media(Base):
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    

    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
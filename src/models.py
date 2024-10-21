import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    datejoined = Column(Date)
    favorites = relationship('Favorites', back_populates='users')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    eye_color = Column(String(20))
    height_cm = Column(Integer)
    birth_year = Column(String(20))
    favorited_by = relationship('Favorites', back_populates='characters')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50))
    diameter = Column(Integer)
    population = Column(Integer)
    favorited_by = relationship('Favorites', back_populates='planets')

class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    users = relationship('User', back_populates='favorites')
    characters = relationship('Character', back_populates='favorited_by')
    planets = relationship('Planet', back_populates='favorited_by')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

from sqlalchemy import Column, Integer, String
from database import Base


class EngineSupported(Base):
    __tablename__ = 'engine_supported'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<EngineSupported %r>' % (self.name)


class Database(Base):
    __tablename__ = 'connection'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    user = Column(String(50), unique=False)
    host = Column(String(120), unique=False)
    password = Column(String(30), unique=False)

    def __repr__(self):
        return '<Database %r>' % (self.name)

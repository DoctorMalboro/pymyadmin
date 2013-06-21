from sqlalchemy import Column, Integer, String
from database import Base, db_session
from saw import DB


class Database(Base):
    query = db_session.query_property()

    __tablename__ = 'connection'
    id = Column(Integer, primary_key=True)
    engine = Column(String(40), unique=False)
    name = Column(String(50), unique=False)
    user = Column(String(50), unique=False)
    host = Column(String(120), unique=False)
    db_name = Column(String(120), unique=False)
    password = Column(String(30), unique=False)

    def __repr__(self):
        return '<Database %r>' % (self.name)

    def connect(self):
        db = DB(
            self.db_name, self.engine, host=self.host,
            password=self.password, username=self.user
        )
        return db

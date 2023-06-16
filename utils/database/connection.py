from sqlalchemy import create_engine, Column, select, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from GAME_OF_TEENS.data import config

db = create_engine(url=config.DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(db)
session = Session()


class Database(Base):
    __tablename__ = 'comments'
    id = Column(BigInteger, primary_key=True)


if __name__ == '__main__':
    print('start')
    Base.metadata.create_all(db)
    select = select(Database)
    print(select)
    users = session.query(Database).all()
    for user in users:
        print(user.id)

    print('finish')

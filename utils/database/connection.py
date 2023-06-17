from sqlalchemy import create_engine, Column, select, BigInteger, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from GAME_OF_TEENS.data import config

db = create_engine(url=config.DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(db)
session = Session()


class Database(Base):
    __tablename__ = 'lifecell_bot'
    id = Column(BigInteger, primary_key=True)
    calls = Column(String, nullable=True)
    internet = Column(String, nullable=True)
    sms = Column(String, nullable=True)
    roaming = Column(Boolean, nullable=True)
    social_pass = Column(Boolean, nullable=True)
    social_platform = Column(Boolean, nullable=True)

    def update_info(self, id=None, calls=None, internet=None,
                    sms=None, roaming=None, social_pass=None, social_platform=None):
        if id:
            self.id = id
        if calls:
            self.calls = calls
        if internet:
            self.internet = internet
        if sms:
            self.sms = sms
        if roaming:
            self.roaming = roaming
        if social_pass:
            self.social_pass = social_pass
        if social_platform:
            self.social_platform = social_platform


if __name__ == '__main__':
    print('start')
    Base.metadata.create_all(db)
    select = select(Database)
    print(select)
    users = session.query(Database).all()
    for user in users:
        print(user.id)

    print('finish')

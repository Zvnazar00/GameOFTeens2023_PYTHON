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
    user_id = Column(BigInteger, primary_key=True)
    calls = Column(String, nullable=True)
    internet = Column(String, nullable=True)
    sms = Column(String, nullable=True)
    social_pass = Column(Boolean, nullable=True)
    social_platform = Column(Boolean, nullable=True)
    categories = Column(String, nullable=True)

    def update_info(self, user_id=None, calls=None, internet=None,
                    sms=None, social_pass=None, social_platform=None, categories=None):
        if user_id:
            self.user_id = user_id
        if calls:
            self.calls = calls
        if internet:
            self.internet = internet
        if sms:
            self.sms = sms
        if social_pass:
            self.social_pass = social_pass
        if social_platform:
            self.social_platform = social_platform
        if categories:
            self.categories = categories


if __name__ == '__main__':
    select = select(Database)
    users = session.query(Database).all()


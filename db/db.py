from sqlalchemy import Column, SmallInteger, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

from config import YEAR, MONTH, DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

Base = declarative_base()


class Book(Base):
    __tablename__ = f'{YEAR}_{MONTH}'

    name = Column(String(50), primary_key=True, nullable=False)
    feat_perfs = Column(SmallInteger)
    secure_perfs = Column(SmallInteger)
    feat_rehs = Column(SmallInteger)
    secure_rehs = Column(SmallInteger)


engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
s = session()

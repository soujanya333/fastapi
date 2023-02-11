from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
from sqlalchemy import Enum, Column, Integer, String, Date




DATABASE_URL = "mysql+pymysql://root:access100@localhost:3306/fastapi"

#DATABASE_URL = "mysql+pymysql://root:access100@localhost:3306/amigaapp"
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




class UserInfo(Base):
    __tablename__ = 'userinfo'

    #id = Column('category_id', Integer, primary_key=True, autoincrement=True)
    id = Column(Integer,primary_key=True, autoincrement=True)
    firstname = Column(String(100), index=True)
    lastname = Column(String(6), index = True)
    email = Column(String(100), index=True)
    mobile_no = Column(String(12), default="")



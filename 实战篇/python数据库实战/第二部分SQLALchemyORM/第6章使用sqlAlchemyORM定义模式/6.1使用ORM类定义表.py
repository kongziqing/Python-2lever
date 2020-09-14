
#定义成ORM类的Cookies表
from sqlalchemy import Table,Column,Integer,Numeric,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Cookie(Base):
    __tablename__='cookies'
    cookie_id = Column(Integer(),primary_key=True)
    cookie_name = Column(String(50),index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12,2))

#另一个拥有更多列的表
from datetime import datetime
from sqlalchemy import DateTime
class User(Base):
    __tablename__='users'
    user_id = Column(Integer(),primary_key=True)
    username=Column(String(15),nullable=False,unique=True)
    email_address = Column(String(255),nullable=False)
    phone = Column(String(20),nullable=False)
    created_on = Column(DateTime(),default=datetime.now)
    updated_on=Column(DateTime(),default=datetime.now,onupdate=datetime.now)

#带关系的表
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,backref
class Order(Base):
    __tablename__='orders'
    order_id = Column(Integer(),primary_key=True)
    user_id = Column(Integer(),ForeignKey('users.user_id'))
    shipped = Column(Boolean(),default=False)

    user = relationship("User",backref=backref('orders',order_by=id))

#带有关系的更多表
class LineItems(Base):
    __tablename__ = 'line_items'
    line_items_id = Column(Integer(),primary_key=True)
    order_id=Column(Integer(),ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(),ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Integer())
    order = relationship("order",backref=backref('line_items',order_by=line_items_id))
    cookie = relationship("Cookie",uselist=False)

#模式持久化
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:8232964kzq@localhost/cookies')
Base.metadata.create_all(engine)


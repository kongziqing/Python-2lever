# import sqlalchemy
# print(sqlalchemy.__version__)
#
# from sqlalchemy import create_engine
# engine = create_engine('mysql+pymysql://root:8232964kzq@localhost/cookies')
#
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
# from sqlalchemy import Column, Integer, String
# from sqlalchemy import Sequence
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(50))
#     fullname = Column(String(50))
#     nickname = Column(String(50))
#
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#                                 self.name, self.fullname, self.nickname)
#
# Base.metadata.create_all(engine)
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
#
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(ed_user)
# session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:8232964kzq@localhost/cookies')
Session=sessionmaker(bind=engine)
session = Session()

from datetime import datetime
from sqlalchemy import (Table,Column,Integer,Numeric,String,DateTime,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref

Base=declarative_base()

class Cookie(Base):
    __tablename__='cookies'
    cookie_id = Column(Integer(),primary_key=True)
    cookie_name = Column(String(50),index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12,2))

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

from sqlalchemy import ForeignKey,Boolean
from sqlalchemy.orm import relationship,backref
class Order(Base):
    __tablename__='orders'
    order_id = Column(Integer(),primary_key=True)
    user_id = Column(Integer(),ForeignKey('users.user_id'))
    shipped = Column(Boolean(),default=False)

    user = relationship("User",backref=backref('orders',order_by=order_id))

#带有关系的更多表
class LineItems(Base):
    __tablename__ = 'line_items'
    line_item_id = Column(Integer(),primary_key=True)
    order_id=Column(Integer(),ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(),ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12,2))
    order = relationship("Order",backref=backref('line_items',order_by=line_item_id))
    cookie = relationship("Cookie",uselist=False,order_by=line_item_id)

Base.metadata.create_all(engine)
#插入单条数据
#cc_cookie = Cookie(cookie_name='chocolate chip',cookie_recipe_url='thhpafafdfa',cookie_sku='CC01',unit_cost=0.50)
#session.add(cc_cookie)
#session.commit()
#插入多条数据
dcc=Cookie(cookie_name='dark chocolate chip',
           cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
           cookie_sku='CC02',
           quantity=1,
           unit_cost=0.75)
mol=Cookie(cookie_name='molasses',
           cookie_recipe_url='http://some.aweso.me/c.html',
           cookie_sku='MOL01',
           quantity=1,
           unit_cost=0.8)
session.add(dcc)
session.add(mol)
#flush()方法和commit()方法相似，但是它不会执行数据库提交并结束事务，因此，dcc和mol实例任然和会话连接，
#你可以使用它们执行更多数据库任务，而无需另外发起数据库查询。
session.flush()
print(dcc.cookie_id)
print(mol.cookie_id)






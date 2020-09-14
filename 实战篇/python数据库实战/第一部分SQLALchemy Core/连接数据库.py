"""
engine = create_engine('dialect+driver://username:password@host:port/database')
dialect -- 数据库类型
driver -- 数据库驱动选择
username -- 数据库用户名
password -- 用户密码
host 服务器地址
port 端口
database 数据库
"""
from sqlalchemy import MetaData
from sqlalchemy import (Table,Column,Integer,Numeric,String,ForeignKey,create_engine,DateTime,Boolean)
from datetime import datetime
#为远程Mysql数据库创建引擎
engine=create_engine('mysql+pymysql://root:8232964kzq@localhost/cookies')
metadata = MetaData()
cookies = Table('cookies',metadata,
                Column('cookie_id',Integer(),primary_key=True),
                Column('cookie_name',String(50),index=True),
                Column('cookie_recipe_url',String(255)),
                Column('cookie_sku',String(55)),
                Column('quantity',Integer()),
                Column('unit_cost',Numeric(12,2)))

users = Table('users',metadata,
              Column('user_id',Integer(),primary_key=True),
              Column('customer_number',Integer(),autoincrement=True),
              Column('username',String(15),nullable=True,unique=True),
              Column('email_address',String(15),nullable=False),
              Column('phone',String(15),nullable=False),
              Column('password',String(25),nullable=False),
              #在设置default和onupdate时使用的是datetime.now,而没有调用datetime.now()函数，如果调用这个函数，
              #它就会把default设置为表首次实例化的时间，通过使用datetime.now,可以得到实例化和更新每个记录的时间
              Column('creat_on',DateTime(),default=datetime.now),
              Column('update_on',DateTime(),default=datetime.now,onupdate=datetime.now))

orders = Table('orders',metadata,
               Column('order_id',Integer(),primary_key=True),
               Column('user_id',ForeignKey('users.user_id')),
               Column('shipped',Boolean(),default=False))

line_items = Table('line_items',metadata,
                   Column('line_items_id',Integer(),primary_key=True),
                   Column('order_id',ForeignKey('orders.order_id')),
                   Column('cookie_id',ForeignKey('cookies.cookie_id')),
                   Column('quantity',Integer()),
                   Column('extended_cost',Numeric(12,2)))

metadata.create_all(engine)



from sqlalchemy import create_engine
import tushare as ts
import datetime
import pandas
import string
import mysql.connector
from sqlalchemy.types import VARCHAR
from sqlalchemy.types import DATE
from sqlalchemy.orm import sessionmaker
import json


pro = ts.pro_api('2f8bb48b37ea2c7bed7b631b5f41ef7c58c94d3de0bb2a72565ea30e')
engine = create_engine('mysql+mysqlconnector://tushare:Tu_123@127.0.0.1/tushare?charset=utf8')
connection = engine.connect()

def getStock():
    stock_init = connection.execute('truncate table l_stock')
    l_stock = pro.stock_basic()
    l_stock.to_sql('l_stock',engine,if_exists='append')

def getTrade():
    l_startdate = connection.execute('select date_add(max(trade_date),interval 1 day) from l_stock_trade')
    for r in l_startdate:
        r1 = r[0]
        r2 = r1.strftime('%Y%m%d')
        print("将从%s开始同步数据"%r2)
    result = connection.execute('select ts_code from l_stock')
    for row in result:
        l_stock_trade = pro.daily(ts_code =row['ts_code'],start_date= r2)
        print(l_stock_trade)
        l_stock_trade.to_sql('l_stock_trade',engine,if_exists='append')
    connection.close()

if __name__ == '__main__':

    #getStock()
    getTrade()




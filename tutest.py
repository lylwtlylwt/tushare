from sqlalchemy import create_engine
import tushare as ts
import mysql.connector
from sqlalchemy.types import VARCHAR

pro = ts.pro_api('2f8bb48b37ea2c7bed7b631b5f41ef7c58c94d3de0bb2a72565ea30e')
engine = create_engine('mysql+mysqlconnector://tushare:Tu_123@127.0.0.1/tushare?charset=utf8')
l_stock = ts.get_stock_basics()
l_stock.to_sql('l_stock',engine,if_exists='replace',dtype={'code':VARCHAR(l_stock.index.get_level_values('code').str.len().max())})

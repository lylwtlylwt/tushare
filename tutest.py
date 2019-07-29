from sqlalchemy import create_engine
import tushare as ts
import mysql.connector
from sqlalchemy.types import VARCHAR
from sqlalchemy.orm import sessionmaker

pro = ts.pro_api('2f8bb48b37ea2c7bed7b631b5f41ef7c58c94d3de0bb2a72565ea30e')
engine = create_engine('mysql+mysqlconnector://tushare:Tu_123@127.0.0.1/tushare?charset=utf8')
connection = engine.connect()
result = connection.execute('select code from l_stock')
for row in result:
    print("stock_code",row['code'])
connection.close()

#Session = sessionmaker(bind = engine)
#session= Session()
#l_code =session.execute('select code from l_stock')
#session.query(l_code).all()
#l_stock = ts.get_stock_basics()
#print(type(l_stock))
#l_stock.to_sql('l_stock',engine,if_exists='replace',dtype={'code':VARCHAR(l_stock.index.get_level_values('code').str.len().max())})

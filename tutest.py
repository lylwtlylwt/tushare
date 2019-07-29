from sqlalchemy import create_engine
import tushare as ts

pro = ts.pro_api('2f8bb48b37ea2c7bed7b631b5f41ef7c58c94d3de0bb2a72565ea30e')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')

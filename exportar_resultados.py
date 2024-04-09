import os
import pandas as pd
import sqlalchemy as sa

BASE_DIR = '.'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BANCO_DIR = 'C:\\Users\\gabriel.castro\\Desktop\\TISS'
engine = sa.create_engine(f'sqlite:///{BANCO_DIR}//banco_tiss.db')
conn = engine.connect()

with open(os.path.join(BASE_DIR, 'procedimentos_media_desvio.sql'), encoding='UTF-8') as file:
    query = file.read()
    df = pd.read_sql_query(query,
                           conn
                           )
    df.to_csv('C:\\Users\\gabriel.castro\\Desktop\\TISS\\procedimentos.csv',
              sep=";",
              decimal=","
              )


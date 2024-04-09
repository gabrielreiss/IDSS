import os
import pandas as pd
import sqlalchemy as sa

BANCO_DIR = 'C:\\Users\\gabriel.castro\\Desktop\\TISS'
engine = sa.create_engine(f'sqlite:///{BANCO_DIR}//banco_tiss.db')
conn = engine.connect()

df = pd.read_csv(os.path.join(BANCO_DIR,"PLANOS.csv"), sep = ";", decimal=",")

df.to_sql("planos", conn)
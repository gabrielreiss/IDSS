import os
import pandas as pd
import sqlalchemy as sa

BASE_DIR = '.'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BANCO_DIR = 'C:\\Users\\gabriel.castro\\Desktop\\TISS'
engine = sa.create_engine(f'sqlite:///{BANCO_DIR}//banco_tiss.db')
conn = engine.connect()


url = 'https://dadosabertos.ans.gov.br/FTP/PDA/caracteristicas_produtos_saude_suplementar/caracteristicas_produtos_saude_suplementar.csv'

df = pd.read_csv(url, sep=";", decimal=",")
df.to_sql("operadoras", conn)
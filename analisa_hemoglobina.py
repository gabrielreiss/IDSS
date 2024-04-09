import os
import pandas as pd
import sqlalchemy as sa

BASE_DIR = '.'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BANCO_DIR = 'C:\\Users\\gabriel.castro\\Desktop\\TISS'
engine = sa.create_engine(f'sqlite:///{BANCO_DIR}//banco_tiss.db')
conn = engine.connect()

df = pd.read_csv(os.path.join(BANCO_DIR, "hemoglobina.csv"),
                 sep=";",
                 decimal=',')

df.head()
df.columns
df.shape

#df.query("ID_PLANO")
planos = df["ID_PLANO"].unique()

with open(os.path.join(BASE_DIR, 'sib.sql')) as file:
    query = file.read()
    df_sib = pd.read_sql_query(query, conn)

df2 = df[df["ID_PLANO"].isin(df_sib['CD_PLANO'])]

#ID_PLANO diferente de CD_PLANO

registro_planos = [469356136,
                   473613153,
                   469359131,
                   480963187,
                   481702188,
                   469227136,
                   469226138,
                   469225130,
                   473522156,
                   480959189]

df[df["ID_PLANO"].isin(registro_planos)]

#não é o número do registro do plano


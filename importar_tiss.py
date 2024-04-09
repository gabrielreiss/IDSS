import os
import pandas as pd
import sqlalchemy as sa

BANCO_DIR = 'C:\\Users\\gabriel.castro\\Desktop\\TISS'
engine = sa.create_engine(f'sqlite:///{BANCO_DIR}//banco_tiss.db')
conn = engine.connect()

url = "https://dadosabertos.ans.gov.br/FTP/PDA/TISS/AMBULATORIAL/2022/RS/"

#RS_202201_AMB_CONS.zip
#RS_202201_AMB_DET.zip

#arquivo = "RS_202201_AMB_DET.zip"

#df.to_parquet(path = "C:\\Users\\gabriel.castro\\Desktop\\TISS\\dados.parquet")

mes = ["01", "02", "03", "04", "05","06","07","08","09","10","11","12"]
tipo = ["DET", "CONS"]
for mes in mes:
    for tipo2 in tipo:
        arquivo = f'RS_2022{mes}_AMB_{tipo2}.zip'
        print(arquivo)
        df = pd.read_csv(f"{url}{arquivo}", compression="zip", sep=";", decimal=",", low_memory=True)
        df.to_sql(f'{tipo2}', conn, if_exists='append')
        del(df)

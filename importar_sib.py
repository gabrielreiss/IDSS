import os
import pandas as pd
import sqlalchemy as sa

BANCO_DIR = 'C:\\Users\\gabriel.castro\\Desktop\\TISS'
engine = sa.create_engine(f'sqlite:///{BANCO_DIR}//banco_tiss.db')
conn = engine.connect()

url = 'https://dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios/'

#202312/
#ben202312_RS.zip
#

mes = ["01", "02", "03", "04", "05","06","07","08","09","10","11","12"]

for mes1 in mes:
    competencia = f'2022{mes1}'
    arquivo = f'ben{competencia}_RS.zip'
    csv = f'{url}{competencia}/{arquivo}'
    print(csv)
    df = pd.read_csv(f'{url}{competencia}/{arquivo}', 
                    compression='zip',
                    low_memory=True,
                    sep=";",
                    decimal=',',
                    date_format="DD/MM/AAAA",
                    encoding='latin-1'
                    )
    df.to_sql("sib", 
              conn,
              if_exists='append'
              )

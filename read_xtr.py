import os
import pandas as pd
import xml.etree.ElementTree as ET

DADOS_DIR = os.path.abspath('C:/Users/gabriel.castro/Desktop/TISS/Retorno')

arquivo = os.path.join(DADOS_DIR, '4175992024010001.XTR')
tree = ET.parse(arquivo)
root = tree.getroot()

#tentativa 1
data = []
for child in root:
    row = {}
    row['name'] = child.attrib['name'] # Accessing an attribute
    row['value'] = child.text # Accessing text content
    data.append(row)

df = pd.DataFrame(data)

#tentativa 2
df = pd.read_xml(arquivo)

# 4175992024010001.XTR

#df = pd.read_xml(os.path.join(DADOS_DIR, '4175992024010001.XTR'))
#df = pd.read_xml(os.path.join(DADOS_DIR, '4175992024018215.XTR'))
#df = pd.read_xml(os.path.join(DADOS_DIR, '4175992024018216.XTR'))

#resumo -> não deu

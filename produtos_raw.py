import pandas as pd
import numpy as np
import os

df = pd.read_csv("datasets/produtos_raw.csv")

df['actual_category'] = (df['actual_category']
                         .str.lower()
                         .str.replace(' ',''))

verificar_colunas = [
    df['actual_category'].str.contains('eletr'),
    df['actual_category'].str.contains('pro'),
    df['actual_category'].str.contains('anco|ncor'),
]

colunas_desejadas = ['eletrônicos', 'propulsão', 'ancoragem']

# df['coluna_normalizada'] = np.select(verificar_colunas, colunas_desejadas, default='Outros')
# print(df['coluna_normalizada'].value_counts())

df['actual_category'] = np.select(verificar_colunas, colunas_desejadas, default='Outros')

df['price'] = (df['price']
                .str.replace('R$', '',regex=False)
                .astype('float64'))

print(df.shape)
print(df.info())

df.drop_duplicates(inplace=True)

print(df.shape)
print(df.info())

pasta_destino = 'CSVs tratados'
arquivo = 'produtos_tratados.csv'
caminho_completo = os.path.join(pasta_destino, arquivo)

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

df_final = df.to_csv(caminho_completo,sep=';', index=False)
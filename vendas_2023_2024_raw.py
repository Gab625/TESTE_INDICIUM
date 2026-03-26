import pandas as pd
import os

df = pd.read_csv('datasets/vendas_2023_2024.csv')
df.head()

df.rename(columns={'id':'sale_id'},inplace=True)

df['sale_date'] = df['sale_date'].str.strip()

df['sale_date'] = pd.to_datetime(df['sale_date'], format='mixed')

pasta_destino = "CSVs_tratados"
arquivo = 'vendas_2023_2024_tratados.csv'
caminho_completo = os.path.join(pasta_destino,arquivo)

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

df_final = df.to_csv(caminho_completo,index=False,sep=';')



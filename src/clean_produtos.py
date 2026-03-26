import pandas as pd
import numpy as np
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
raw_data_path = root_dir / 'data' / '1_raw'
processed_data_path = root_dir / 'data' / '2_processed'

df = pd.read_csv(raw_data_path/"produtos_raw.csv")

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

df.rename(columns={'code':'id_product','name':'product_name'}, inplace=True)

processed_data_path.mkdir(parents=True, exist_ok=True)

df_final = df.to_csv(processed_data_path/'produtos_tratados.csv',sep=';', index=False)
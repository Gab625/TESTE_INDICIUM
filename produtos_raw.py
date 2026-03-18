import pandas as pd
import numpy as np

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

df['actual_category'] = np.select(verificar_colunas, colunas_desejadas, default='Outros')

df['price'] = (df['price']
               .str.replace('R$', '',regex=False)
               .astype('float64'))

print(df.shape)
print(df.info())

df.drop_duplicates(inplace=True)

print(df.shape)
print(df.info())
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('datasets/vendas_2023_2024.csv')

matriz = pd.crosstab(df['id_client'], df['id_product'])
matriz_presenca = (matriz >  0).astype(int)

similarity = cosine_similarity(matriz_presenca.T)

df_similarity = pd.DataFrame(
    similarity, 
    index=matriz_presenca.columns, 
    columns=matriz_presenca.columns
)

produto_alvo = 27

similares = df_similarity[produto_alvo].sort_values(ascending=False)

df_produtos = pd.read_csv('concluidos/produtos_raw_tratados.csv')
df_produtos.rename(columns={'code':'id_product'}, inplace=True)

df_final = pd.merge(similares, df_produtos, on='id_product')
df_final.rename(columns={27:'similaridade'},inplace=True)

print(f"Produtos que costumam sair junto com o product_id {produto_alvo}:")
print(df_final.iloc[0:6])

df_final.to_csv('similares_a_GPS_Garmin.csv',index=False)


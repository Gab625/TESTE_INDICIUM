import pandas as pd

df_vendas = pd.read_csv("datasets/vendas_2023_2024.csv")
df_dias = pd.read_csv('dia_semana.csv')

df_dias.rename(columns={'data':'sale_date'}, inplace=True)

df_final = pd.merge(df_dias,df_vendas,on='sale_date', how='left')
df_final.isnull().sum()

df_final = df_final.fillna(0)
df_final.isnull().sum()

df_diario = df_final.groupby(['sale_date', 'id_product'])['qtd'].sum().reset_index()

ultima_semana_2023 = df_diario[
    (df_diario['sale_date'] >= '2023-12-25') & 
    (df_diario['sale_date'] < '2024-01-01')
]

baseline_produtos = ultima_semana_2023.groupby('id_product')['qtd'].mean().reset_index()
baseline_produtos.rename(columns={'qtd':'media_diaria'}, inplace=True)

periodo_janeiro = pd.date_range(start='2024-01-01', end='2024-01-31')
df_calendario_janeiro = pd.DataFrame({'sale_date':periodo_janeiro})

df_calendario_janeiro['key'] = 1
baseline_produtos['key'] = 1

previsao_diaria = pd.merge(df_calendario_janeiro, baseline_produtos, on='key').drop('key', axis=1)

previsao_diaria['previsao_venda_diaria'] = previsao_diaria['media_diaria'].round(0)

df_produtos = pd.read_csv('concluidos/produtos_raw_tratados.csv')
df_produtos.rename(columns={'code':'id_product'},inplace=True)

df_final = pd.merge(previsao_diaria,df_produtos,on='id_product',how='left')

colunas_finais = ['sale_date', 'id_product', 'name', 'previsao_venda_diaria']
df_relatorio = df_final[colunas_finais]

venda_semanal_motor155hp = df_relatorio[
    (df_relatorio['id_product'] == 54.0) & 
    (df_relatorio['sale_date'] >= '2024-01-01') & 
    (df_relatorio['sale_date'] <= '2024-01-07')
]

total_previsao = venda_semanal_motor155hp['previsao_venda_diaria'].sum()

print(f"Previsão total para semana de janeiro: {int(total_previsao)}")
import pandas as pd

df = pd.read_json("datasets/custos_importacao.json")
df_explode_historic = df.explode('historic_data').reset_index(drop=True)

df_historic_data = pd.json_normalize(df_explode_historic['historic_data'])

df_final = pd.concat([df_explode_historic.drop('historic_data', axis=1), df_historic_data], axis=1)

df_final['start_date'] = pd.to_datetime(df_final['start_date'], dayfirst=True)

df_final.to_csv('custo_importacao_tratados.csv', index=False, sep=";", encoding='utf-8-sig')
df_final.info()
import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
raw_data_path = root_dir / 'data' / '1_raw'
processed_data_path = root_dir / 'data' / '2_processed'

df = pd.read_csv(raw_data_path/'vendas_2023_2024.csv')
df.head()

df.rename(columns={'id':'sale_id'},inplace=True)

df['sale_date'] = df['sale_date'].str.strip()

df['sale_date'] = pd.to_datetime(df['sale_date'], format='mixed')

processed_data_path.mkdir(parents=True, exist_ok=True)

df_final = df.to_csv(processed_data_path/'vendas_tratados.csv',index=False,sep=';')



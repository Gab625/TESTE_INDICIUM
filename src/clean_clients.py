import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
raw_data_path = root_dir / 'data' / '1_raw'
processed_data_path = root_dir / 'data' / '2_processed'

df = pd.read_json(raw_data_path / 'clientes_crm.json')
df.head()

df.rename(columns={'code': 'id_client'}, inplace=True)

df['email'] = df['email'].str.replace({'#': '@'}, regex=True)

df['location'] = df['location'].str.replace(r'[,/]', '-', regex=True)

df_split = df['location'].str.split('-', n=1, expand=True)

def ajustar_ordem(row):
    p1, p2 = row[0].strip(), row[1].strip() if row[1] else ""
    return (p2, p1) if len(p1) == 2 else (p1, p2)

df[['city', 'state']] = df_split.apply(ajustar_ordem, axis=1, result_type='expand')

df['city'] = df['city'].str.replace(r'\(.*?\)', '', regex=True).str.strip()

df['state'] = df['state'].str.upper()
df = df.drop('location',axis=1)

df.info()
df.isnull().sum()

df['city'] = df['city'].str.upper().str.strip()
df['state'] = df['state'].str.upper().str.strip()

verificar_tratamento_state = df[df['state'].str.len()!=2]
verificar_tratamento_state

processed_data_path.mkdir(parents=True, exist_ok=True)

df_final = df.to_csv(processed_data_path/'clientes_tratados.csv',sep=';', index=False)



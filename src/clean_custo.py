# Importando a biblioteca pandas para manipulação de dados
import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
raw_data_path = root_dir / 'data' / '1_raw'
processed_data_path = root_dir / 'data' / '2_processed'

# Lendo o arquivo JSON e armazenando em um DataFrame
df = pd.read_json(raw_data_path/"custos_importacao.json")
df.head()

# Explodindo a coluna 'historic_data' para criar uma linha para cada item da lista
df_explode_historic = df.explode('historic_data').reset_index(drop=True)

# Normalizando a coluna 'historic_data' para criar colunas separadas para cada chave do dicionário e 
# exibindo as primeiras linhas do DataFrame resultante
df_historic_data = pd.json_normalize(df_explode_historic['historic_data'])
df_historic_data.head()

# Concatenando o DataFrame original (sem a coluna 'historic_data') com o DataFrame normalizado para obter um DataFrame final
df_final = pd.concat([df_explode_historic.drop('historic_data', axis=1), df_historic_data], axis=1)

# Convertendo a coluna 'start_date' para o formato datetime, considerando o formato dia/mês/ano
df_final['start_date'] = pd.to_datetime(df_final['start_date'], dayfirst=True)

processed_data_path.mkdir(parents=True, exist_ok=True)

# Exportando o DataFrame final para um arquivo CSV, sem o índice, usando ponto e vírgula como separador e codificação UTF-8
# Verificando se a pasta de destino existe, e se não existir, criando-a
# Exportando o DataFrame final para um arquivo CSV, sem o índice, usando ponto e vírgula como separador e codificação UTF-8
df_final.to_csv(processed_data_path/'custo_importacao_tratados.csv', index=False, sep=";", encoding='utf-8-sig')
df_final.info()



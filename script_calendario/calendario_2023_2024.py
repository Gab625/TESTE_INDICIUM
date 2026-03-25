import pandas as pd
from pathlib import Path

datas = pd.date_range(start='2023-01-01', end='2024-12-31')
df_calendario = pd.DataFrame(datas, columns=['data'])

meses_pt = {
    'January':'Janeiro','February':'Fevereiro','March':'Marco','April':'Abril','May':'Maio',
    'June':'Junho','July':'Julho','August':'Agosto','September':'Setembro','October':'Outubro',
    'November':'Novembro','December':'Dezembro'
}

dias_pt = {
    'Monday':'Segunda-feira','Tuesday':'Terca-feira','Wednesday':'Quarta-feira',
    'Thursday':'Quinta-feira','Friday':'Sexta-feira','Saturday':'Sabado','Sunday':'Domingo'
}

df_calendario['ano'] = df_calendario['data'].dt.year
df_calendario['mes'] = df_calendario['data'].dt.month
df_calendario['nome_mes'] = df_calendario['data'].dt.month_name().map(meses_pt)
df_calendario['dia_semana'] = df_calendario['data'].dt.day_name().map(dias_pt)
df_calendario['data'] = df_calendario['data'].dt.date

raiz_projeto = Path(__file__).resolve().parent.parent

pasta_destino = raiz_projeto / 'CSVs Tratados'
arquivo_final = pasta_destino / 'calendar_2023_2024.csv'

pasta_destino.mkdir(parents=True,exist_ok=True)

df_final = df_calendario.to_csv(arquivo_final, sep=';',index=False)
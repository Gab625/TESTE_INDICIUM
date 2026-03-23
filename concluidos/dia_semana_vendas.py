import pandas as pd
from sqlalchemy import create_engine

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

engine = create_engine('postgresql://postgres:pradog23029@localhost:5432/db_vendas_2023_2024')
df_calendario.to_sql('dim_calendario', engine, if_exists='replace', index=False)
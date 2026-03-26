import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
processed_data_path = root_dir / 'data' / '2_processed'

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

processed_data_path.mkdir(parents=True, exist_ok=True)

df_final = df_calendario.to_csv(processed_data_path/'calendar_2023_2024.csv', sep=';',index=False)
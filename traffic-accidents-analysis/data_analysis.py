import pandas as pd

"""
este módulo é responsável pela análise exploratória dos dados 
e criação de colunas auxiliares para facilitar análises temporais
"""

# função para preparar e criar colunas relacionadas ao tempo no data frame
def prepare_time_features(df):
    # converte a coluna 'Start_Time' para datetime, permitindo extração de componentes temporais
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['Date'] = df['Start_Time'].dt.date # cria uma nova coluna apenas com a data (sem hora)
    df['Hour'] = df['Start_Time'].dt.hour # cria uma nova coluna com a hora do evento (0-23)
    df['Day_of_Week'] = df['Start_Time'].dt.day_name() # cria uma coluna com o nome do dia da semana (monday, tuesday, etc)

    # cria uma coluna categórica 'Time_of_Day' dividindo em 'Day' (6h às 18h) ou 'Night' (18h às 6h)
    df['Time_of_Day'] = ['Day' if 6 <= t.hour < 18 else 'Night' for t in df['Start_Time']]
    
    return df

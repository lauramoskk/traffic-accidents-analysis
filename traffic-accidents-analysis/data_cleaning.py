import pandas as pd

# este módulo é responsável pela leitura e limpeza dos dados do dataset de acidentes

# função para carregar o dataset a partir de um arquivo CSV
def load_data(filepath):
    return pd.read_csv(filepath)

# função para limpar o data frame removendo duplicatas e tratando valores nulos
def clean_data(df):
    df = df.drop_duplicates() # remove linhas duplicadas

    # lista das colunas numéricas que terão valores nulos preenchidos
    cols_to_fill = ['Wind_Speed(mph)', 'Temperature(F)', 'Wind_Chill(F)','Humidity(%)', 'Pressure(in)', 'Visibility(mi)']
    
    # para cada coluna na lista, preenche os valores nulos com a mediana daquela coluna
    for col in cols_to_fill:
        df[col] = df[col].fillna(df[col].median())

    return df # retorna o data frame limpo e com valores preenchidos

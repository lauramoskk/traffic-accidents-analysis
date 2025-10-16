from data_cleaning import load_data, clean_data
from data_analysis import prepare_time_features
from visualizations import plot_top_states, plot_weather_severity, plot_map

# 1. carregar dados brutos
# lê o arquivo CSV de acidentes de trânsito e carrega em um data frame
df = load_data('data/us_traffic_accidents_march23.csv')

# 2. limpar dados
# remove duplicatas e preenche valores ausentes com a mediana
df = clean_data(df)

# 3. preparar colunas auxiliares
# cria novas colunas relacionadas ao tempo (dia da semana, hora do dia, etc)
df = prepare_time_features(df)

# 4. visualizações exploratórias
plot_top_states(df) 
plot_weather_severity(df) 
plot_map(df) 

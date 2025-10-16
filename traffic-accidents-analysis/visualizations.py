import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""
este módulo é responsável por gerar visualizações, incluindo gráficos estáticos e mapas
interativos, para auxiliar na análise exploratória dos acidentes de trânsito
"""

# função que plota um gráfico de pizza mostrando os 3 estados com mais acidentes
def plot_top_states(df):
    # conta quantos acidentes ocorreram por estado e seleciona os 3 com maior número
    top_estados = df['State'].value_counts().head(3) 
    
    plt.figure(figsize=(8, 5))
    
    # cria uma paleta de cores para os pedaços do gráfico de pizza
    colors = sns.color_palette("Set3", n_colors=len(top_estados)) 
    
    # plota o gráfico de pizza com rótulos e porcentagens
    plt.pie(top_estados, labels=top_estados.index, autopct='%1.1f%%', startangle=140, colors=colors) 
    
    plt.title('Top 3 Estados com mais acidentes') 
    plt.axis('equal') # garante que o gráfico seja um círculo
    plt.show()

# função que plota um gráfico de barras mostrando a gravidade média dos acidentes por condição climática
def plot_weather_severity(df):
    # agrupa os dados pela condição climática e calcula a média da gravidade
    severity_by_weather = df.groupby('Weather_Condition')['Severity'].mean().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    
    # plota um gráfico de barras horizontal com uma paleta de cores do frio para o quente
    sns.barplot(x=severity_by_weather.values, y=severity_by_weather.index, palette="coolwarm")

    plt.title('Gravidade média por condição climática')
    plt.xlabel('Gravidade média')
    plt.ylabel('Condição climática')
    plt.show()

# plota um mapa interativo dos acidentes nos EUA, colorido pela gravidade
def plot_map(df):
    fig = px.scatter_mapbox(
        df, lat='Start_Lat', # latitude dos acidentes
        lon='Start_Lng', # longitude dos acidentes
        color='Severity', # cor dos pontos baseada na gravidade
        hover_name='City', # informação mostrada ao passar o mouse
        hover_data={'Severity': True, 'Temperature(F)': True, 'Humidity(%)': True},
        color_continuous_scale=px.colors.sequential.Rainbow,
        zoom=3, # zoom inicial do mapa
        title='Mapa Interativo de Acidentes'
    )

    # define o estilo e o centro do mapa para os EUA
    fig.update_layout(mapbox_style='carto-positron', mapbox_center={"lat": 37.0902, "lon": -95.7129})
    
    fig.show()

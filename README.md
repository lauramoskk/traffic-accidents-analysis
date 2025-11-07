# Análise de acidentes de trânsito nos Estados Unidos

### Descrição

Este projeto tem como objetivo analisar dados reais de acidentes de trânsito ocorridos nos Estados Unidos, explorando **padrões, tendências e fatores que influenciam a gravidade** dos acidentes.  

A análise considera variáveis como **condições climáticas, localização geográfica, horário do dia, visibilidade e sinalização de trânsito**, permitindo identificar **momentos e locais mais críticos** para a segurança viária.

O projeto foi desenvolvido inicialmente no **Google Colab**, ambiente ideal para testes e exploração de dados de forma rápida e colaborativa. Em seguida, foi reestruturado em **arquivos Python organizados** para facilitar a manutenção, reaproveitamento de código e execução local.

A análise inclui:
- Limpeza e tratamento de dados com **Pandas**.
- Análise exploratória e criação de colunas auxiliares para análise temporal.
- Visualizações com **Seaborn** e **Matplotlib**.
- Mapa interativo com **Plotly**, destacando a gravidade dos acidentes em diferentes regiões.

[Acesse a versão no Colab](https://colab.research.google.com/drive/1Ik8QIjshpLZmoFXzDceXt7hOV7YPKQBP)

<br>

<img width="600" height="574" alt="top_states" src="https://github.com/user-attachments/assets/eeaf4f69-b19d-4448-a136-9f08646d6b6d" />
<img width="600" height="674" alt="weather_severity" src="https://github.com/user-attachments/assets/c2407986-64d8-4458-bcce-5f6f9ff07d19" />
<img width="600" height="952" alt="map" src="https://github.com/user-attachments/assets/6e51908c-8175-4e5f-99f2-ddf8809f12b0" />

<br>
<br>
<br>

### Instruções de execução

```bash
# 1. Clone o repositório e acesse a pasta:
git clone https://github.com/seu-usuario/traffic-accidents-analysis.git
cd traffic-accidents-analysis

# 2. Instale as dependências necessárias:
pip install pandas seaborn matplotlib plotly

# 3. Execute o script principal:
python main.py
```


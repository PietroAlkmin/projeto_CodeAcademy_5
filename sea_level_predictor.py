import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    #Vou ler os dados do csv
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #Aqui estamos gerando o grafico de dispersão com a finalidade de enxergarmos como os dados estao distribuidos
    plt.figure(figsize=(12, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])# Esse grafico vai ficar em funcao de ano, com o a coluna CSIRO Adjusted Sea Level como o y

    # Create first line of best fit
    # Aqui estou usando a regressao linear para calcular a funcao que vai representar o sea level ate 2050 usando os dados de (1880-2013)
    # isso vai me dar a inclinacao e interseccao da linha de tendencia
    m, b, _, _, _  = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])#nessa linha nos estamos calculando a inclinacao da reta(m) e onde a reta cruza o eixo Y quando x = 0
    years_extended = range(1880, 2051)# estendo a previsao ate 2050 usando a formula da linha reta
    line1 = [m * year + b for year in years_extended]# Aqui estou calculando a linha de previsão aplicando a formula da reta, onde a inclinação da reta(slope) multiplica o ano + ponto de interseção entre os dois eixos (ano, Sea Level adjusted)
    plt.plot(years_extended, line1, 'r', label='2050 Sea Level Prediction (1880-2050)')#Aqui estou criando o gráfico que representa essa previsão

    # Create second line of best fit
    # Aqui estou fazendo outra regressao com os dados mais recentes (de 2000 pra frente) para verificar o impacto que as mudanças climáticas recentes vao ter no longo prazo em comparacao com a outra previsao mais abrangente 
    # Essa abordagem vai mostrar se a tendencia mudou nos ultimos anos
    df_recent = df[df['Year'] >= 2000]#Aqui estou considerando dados somente a partir de 2000
    m_2, b_2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    line2 = [ m_2 * year + b_2 for year in years_recent]
    plt.plot(years_recent, line2, 'b', label='2050 Sea Level Prediction (2000-2050)')

    # Add labels and title
    # adicionando os titulos e descricoes que os testes requerem 
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
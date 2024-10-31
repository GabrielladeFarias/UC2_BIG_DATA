import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_cvli = df_ocorrencias[['aisp','cvli']]
df_cvli = df_cvli.groupby(['aisp']).sum(['cvli']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cvli.head())

# Criando o array dos roubos de veiculos
array_cvli = np.array(df_cvli["cvli"])

# Obtendo a média dos roubos de veiculos
media_cvli = np.mean(array_cvli)

# Obtendo a mediana dos roubos de veiculos
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude dos roubos de veiculos
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame roubos de veículos
df_cvli_outliers_superiores = df_cvli[df_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_cvli[df_cvli['cvli'] < limite_inferior_cvli]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_cvli = np.var(array_cvli)
distancia_var_cvli = variancia_cvli / (media_cvli**2)
desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli



# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS DE VEÍCULOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média de Crimes Violentos Letais Intencionais é {media_cvli:.0f}")
print(f"A mediana de Crimes Violentos Letais Intencionais é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana é de Crimes Violentos Letais Intencionais é {distancia_cvli:.2f} %")
print(f"O menor valor de Crimes Violentos Letais Intencionais é {minimo_cvli:.0f}")
print(f"O maior valor de Crimes Violentos Letais Intencionais é {maximo_cvli:.0f}")
print(f"A amplitude dos valores de Crimes Violentos Letais Intencionais é {amplitude_cvli:.0f}")
print(f"O valor do q1 - 25% de Crimes Violentos Letais Intencionais é {q1_cvli:.0f}")
print(f"O valor do q2 - 50% de Crimes Violentos Letais Intencionais é {q2_cvli:.0f}")
print(f"O valor do q3 - 75% de Crimes Violentos Letais Intencionais é {q3_cvli:.0f}")
print(f"O valor do iqr = q3 - q1 de Crimes Violentos Letais Intencionais é {iqr_cvli:.0f}")
print(f"O limite inferior de Crimes Violentos Letais Intencionais é {limite_inferior_cvli:.0f}")
print(f"O limite superior de Crimes Violentos Letais Intencionais é {limite_superior_cvli:.0f}")
print(f"A variância de Crimes Violentos Letais Intencionais é {variancia_cvli:.0f}")
print(f"A distância da variância X média de Crimes Violentos Letais Intencionais é {distancia_var_cvli:.0f}")
print(f"O desvio padrão de Crimes Violentos Letais Intencionais é {desvio_padrao_cvli:.0f}")
print(f"O coeficiente de variação de Crimes Violentos Letais Intencionais é {coeficiente_var_cvli:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise de Crimes Violentos Letais Intencionais')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('BoxPlot de Crimes Violentos Letais Intencionais')
plt.boxplot(array_cvli,vert=False,showmeans=True)


# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('Histograma de Crimes Violentos Letais Intencionais')
plt.hist(array_cvli,bins=100,edgecolor='black', color= 'purple')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,2)
df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
plt.title('Ranking dos Batalhões com Outliers Superiores')
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'], color= 'pink', edgecolor= 'red')


# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,3)
plt.title('Medidas Descritivas de Crimes Violentos Letais Intencionais')
plt.axis('off')
plt.text(0.1,0.8,f'Média de Crimes Violentos Letais Intencionais {media_cvli:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Mediana de Crimes Violentos Letais Intencionais {mediana_cvli:.0f}',fontsize=12)
plt.text(0.1,0.6,f'Distância entre Média e Mediana de Crimes Violentos Letais Intencionais {distancia_cvli:.2f}%',fontsize=12)
plt.text(0.1,0.5,f'Maior valor de Crimes Violentos Letais Intencionais {maximo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Menor valor de Crimes Violentos Letais Intencionais {minimo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.3,f'Distância entre a Variância e Média de Crimes Violentos Letais Intencionais {distancia_var_cvli:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Coeficiente de variação de Crimes Violentos Letais Intencionais {coeficiente_var_cvli:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
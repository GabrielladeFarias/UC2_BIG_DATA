import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_rec_veiculo = df_ocorrencias[['aisp','ano','recuperacao_veiculos']]
df_rec_veiculo = df_rec_veiculo[df_rec_veiculo['ano'].isin([2022,2023])] # Comando para filtrar por anos (isin([ano utilizado]))
df_rec_veiculo = df_rec_veiculo.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()

# Para maior filtro
df_rec_veiculo_ano = df_ocorrencias[['aisp','ano','recuperacao_veiculo']]
df_rec_veiculo_ano = df_rec_veiculo_ano.groupby(['ano']).sum(['recuperacao_veiculos']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_rec_veiculo.head())

# Criando o array dos roubos de veiculos
array_rec_veiculo = np.array(df_rec_veiculo["recuperacao_veiculos"])

# Obtendo a média dos roubos de veiculos
media_rec_veiculo = np.mean(array_rec_veiculo)

# Obtendo a mediana dos roubos de veiculos
mediana_rec_veiculo = np.median(array_rec_veiculo)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_rec_veiculo = abs((media_rec_veiculo - mediana_rec_veiculo) / mediana_rec_veiculo) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_rec_veiculo = np.max(array_rec_veiculo)
minimo_rec_veiculo = np.min(array_rec_veiculo)

# Obtendo a amplitude dos roubos de veiculos
amplitude_rec_veiculo = maximo_rec_veiculo - minimo_rec_veiculo

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_rec_veiculo = np.quantile(array_rec_veiculo, 0.25, method='weibull')
q2_rec_veiculo = np.quantile(array_rec_veiculo, 0.50, method='weibull')
q3_rec_veiculo = np.quantile(array_rec_veiculo, 0.75, method='weibull')
iqr_rec_veiculo = q3_rec_veiculo - q1_rec_veiculo

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_rec_veiculo = q3_rec_veiculo + (1.5 * iqr_rec_veiculo)
limite_inferior_rec_veiculo = q1_rec_veiculo - (1.5 * iqr_rec_veiculo)

# Filtrando o DataFrame roubos de veículos
df_rec_veiculo_outliers_superiores = df_rec_veiculo[df_rec_veiculo['recuperacao_veiculos'] > limite_superior_rec_veiculo]
df_rec_veiculo_outliers_inferiores = df_rec_veiculo[df_rec_veiculo['recuperacao_veiculos'] < limite_inferior_rec_veiculo]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_rec_veiculo = np.var(array_rec_veiculo)
distancia_var_rec_veiculo = variancia_rec_veiculo / (media_rec_veiculo**2)
desvio_padrao_rec_veiculo = np.std(array_rec_veiculo)
coeficiente_var_rec_veiculo = desvio_padrao_rec_veiculo / media_rec_veiculo



# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE RECUPERACAO DE VEÍCULOS ROUBADOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média da Recuperação dos Veículos Roubados é é {media_rec_veiculo:.0f}")
print(f"A mediana da Recuperação dos Veículos Roubados é é {mediana_rec_veiculo:.0f}")
print(f"A distância entre a média e a mediana é da Recuperação dos Veículos Roubados é é {distancia_rec_veiculo:.2f} %")
print(f"O menor valor da Recuperação dos Veículos Roubados é é {minimo_rec_veiculo:.0f}")
print(f"O maior valor da Recuperação dos Veículos Roubados é é {maximo_rec_veiculo:.0f}")
print(f"A amplitude dos valores da Recuperação dos Veículos Roubados é é {amplitude_rec_veiculo:.0f}")
print(f"O valor do q1 - 25% da Recuperação dos Veículos Roubados é é {q1_rec_veiculo:.0f}")
print(f"O valor do q2 - 50% da Recuperação dos Veículos Roubados é é {q2_rec_veiculo:.0f}")
print(f"O valor do q3 - 75% da Recuperação dos Veículos Roubados é é {q3_rec_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 da Recuperação dos Veículos Roubados é é {iqr_rec_veiculo:.0f}")
print(f"O limite inferior da Recuperação dos Veículos Roubados é é {limite_inferior_rec_veiculo:.0f}")
print(f"O limite superior da Recuperação dos Veículos Roubados é é {limite_superior_rec_veiculo:.0f}")
print(f"A variância da Recuperação dos Veículos Roubados éé {variancia_rec_veiculo:.0f}")
print(f"A distância da variância X média da Recuperação dos Veículos Roubados é é {distancia_var_rec_veiculo:.0f}")
print(f"O desvio padrão da Recuperação dos Veículos Roubados é é {desvio_padrao_rec_veiculo:.0f}")
print(f"O coeficiente de variação da Recuperação dos Veículos Roubados é {coeficiente_var_rec_veiculo:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_rec_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_rec_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_rec_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_rec_veiculo_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre a Recuperação dos Veículos Roubados')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot da Recuperação dos Veículos Roubados')
plt.boxplot(array_rec_veiculo,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Histograma da Recuperação dos Veículos Roubados')
plt.hist(array_rec_veiculo,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
plt.title('Ranking das Batalhões com Outliers Superiores')
df_rec_veiculo_outliers_superiores_order = df_rec_veiculo_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.barh(df_rec_veiculo_outliers_superiores_order['aisp'].astype(str),df_rec_veiculo_outliers_superiores_order['recuperacao_veiculos'])
plt.plot(df_rec_veiculo_ano['ano'].astype(str),df_rec_veiculo_ano['recuperacao_veiculos'])


# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas de Recuperação dos Veículos Roubados')
plt.axis('off')
plt.text(0.1,0.9,f'Média de Recuperação dos Veículos Roubados {media_rec_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana de Recuperação dos Veículos Roubados {mediana_rec_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana de Recuperação dos Veículos Roubados {distancia_rec_veiculo:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor de Recuperação dos Veículos Roubados {maximo_rec_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor de Recuperação dos Veículos Roubados {minimo_rec_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média de Recuperação dos Veículos Roubados {distancia_var_rec_veiculo:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação de Recuperação dos Veículos Roubados {coeficiente_var_rec_veiculo:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
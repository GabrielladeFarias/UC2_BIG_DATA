import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print('-------------- OBTENDO DADOS -------------')

endereco_dados = 'BASES\Titanic.csv'
df_titanic = pd.read_csv(endereco_dados, sep= ';', encoding= 'iso-8859-1')
df_fare_age = df_titanic[['Name','Age','Fare','Survived']] # Filtra os dados

print('----------------- EXIINDO A BASE DE DADOS ------------------')
print(df_titanic.head())

array_tarifas = np.array(df_titanic['Fare'])
array_idades = np.array(df_titanic['Age'])

#Obtendo média e mediana do valor das passagens.

media_tarifas = np.mean(array_tarifas)
mediana_tarifas = np.median(array_tarifas)
distancia_tarifas = abs((media_tarifas - mediana_tarifas) / mediana_tarifas)* 100
#Obtendo o máximo e o minimo do valor das passagens

maximo_tarifas = np.max(array_tarifas)
minimo_tarifas = np.min(array_tarifas)
amplitude_tarifas = maximo_tarifas - minimo_tarifas

#Obtendo média e medianan

media_idades = np.mean(array_idades)
mediana_idades = np.median(array_idades)
distancia_idades = abs((media_idades - mediana_idades) / mediana_idades)* 100
# Obtemdo o máximo e o mínimo das idades

maximo_idades = np.max(array_idades)
minimo_idades = np.min(array_idades)
amplitude_idades = maximo_idades - minimo_idades

# Obtendo os Quartis das idades e tarifas

q1_tarifas = np.quantile(array_tarifas, 0.25, method='weibull') 
q2_tarifas = np.quantile(array_tarifas, 0.50, method='weibull')
q3_tarifas = np.quantile(array_tarifas, 0.75, method='weibull')
iqr_tarifas = q3_tarifas - q1_tarifas  

q1_idades = np.quantile(array_idades, 0.25, method='weibull')
q2_idades = np.quantile(array_idades, 0.50, method='weibull')
q3_idades = np.quantile(array_idades, 0.75, method='weibull')
iqr_idades = q3_idades - q1_idades

#Identificando os os outliers superiores e inferiores da renda e do valor emprestado
limite_superior_tarifas = q3_tarifas + (1.5 * iqr_tarifas)
limite_inferior_tarifas = q1_tarifas - (1.5 * iqr_tarifas)

limite_superior_idades = q3_idades + (1.5 * iqr_idades)
limite_inferior_idades = q1_idades - (1.5 * iqr_idades)

# Filtrando o DataFrame Financeira
df_titanic_tarifas_outliers_superiores = df_fare_age[df_fare_age['Fare'] > limite_superior_tarifas]
df_titanic_tarifas_outliers_inferiores = df_fare_age[df_fare_age['Fare'] < limite_inferior_tarifas]

df_titanic_idades_outliers_superiores = df_fare_age[df_fare_age['Age'] > limite_superior_idades]
df_titanic_idades_outliers_inferiores = df_fare_age[df_fare_age['Age'] < limite_inferior_idades]

# Obtendo as medias de dispersão das passagens
variancia_tarifa = np.var(array_tarifas)
distancia_var_tarifa = variancia_tarifa / (media_tarifas**2) #Fórmula matemática para calcular a distancia
desvio_padrao_tarifa = np.std(array_tarifas)
coeficiente_var_tarifa = desvio_padrao_tarifa / media_tarifas

# Obtendo as medias de dispersão das idades
variancia_idades = np.var(array_idades)
distancia_var_idades = variancia_idades / (media_idades**2) #Fórmula matemática para calcular a distancia
desvio_padrao_idades = np.std(array_idades)
coeficiente_var_idades = desvio_padrao_idades / media_idades


print('\n---------- DADOS DE EMBARQUE: TARIFAS ----------')
print(f"A média das Tarifas é R$ {media_tarifas:.2f}")
print(f"A mediana das Tarifas é R$ {mediana_tarifas:.2f}")
print(f"A distancia entre a média e a mediana é {distancia_tarifas:.2f}%")
print(f"O maior valor das passagens  é R$ {maximo_tarifas:.2f}") 
print(f"O menor valor das passagens é R$ {minimo_tarifas:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_tarifas:.2f}")
print('\n')

print('\n---------- Medidas de Tendência Central -----------')
print(f"O valor do Q1 - 25% das Tarifas é R$ {q1_tarifas:.2f}")
print(f"O valor do Q2 - 50% das Tarifas é R$ {q2_tarifas:.2f}")
print(f"O valor do Q3 - 75% das Tarifas é R$ {q3_tarifas:.2f}")
print(f"O valor do IQR = Q3 - Q1 das Tarifas é R$ {iqr_tarifas:.2f}")
print(f"O limite inferior das Tarifas é R$ {limite_inferior_tarifas:.2f}")
print(f"O limite superior das Tarifas é R$ {limite_superior_tarifas:.2f}")
print(f"A variância das tarifas dos passageiros é {variancia_tarifa:.2f}")
print(f"A distância da variância X média das tarifas dos passageiros é {distancia_var_tarifa:.2f}")
print(f"O desvio padrão das tarifas dos passageiros é {desvio_padrao_tarifa:.2f}")
print(f"O coeficiente de variação das tarifas dos passageiros é {coeficiente_var_tarifa:.2f}")


print('\n- Verificando a existência de outliers inferiores -')
if len(df_titanic_tarifas_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_titanic_tarifas_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_titanic_tarifas_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_titanic_tarifas_outliers_superiores)

print('\n---------- DADOS DE EMBARQUE: IDADES ----------')
print(f"A média das Idades é {media_idades:.2f}")
print(f"A mediana das Idades é {mediana_idades:.2f}")
print(f"A distancia entre a média e a mediana das idades é {distancia_idades:.2f}%")
print(f"A maior idade entre os passageiros é {maximo_idades:.2f}") 
print(f"A menor idade entre os passageiros é {minimo_idades:.2f}")
print(f"A amplitude entre as idades é {amplitude_idades:.2f}")
print('\n')

print('\n---------- Medidas de Tendência Central -----------')
print(f"O valor do Q1 - 25% das Idades é {q1_idades:.2f}")
print(f"O valor do Q2 - 50% das Idades é {q2_idades:.2f}")
print(f"O valor do Q3 - 75% das Idades é {q3_idades:.2f}")
print(f"O valor do IQR = Q3 - Q1 das Idades é {iqr_idades:.2f}")
print(f"O limite inferior das Idades é {limite_inferior_idades:.2f}")
print(f"O limite superior das Idades é {limite_superior_idades:.2f}")
print(f"A variância entre as idades dos passageiros é {variancia_idades:.2f}")
print(f"A distância da variância X média entre as idades dos passageiros é {distancia_var_idades:.2f}")
print(f"O desvio padrão entre as idades dos passageiros é {desvio_padrao_idades:.2f}")
print(f"O coeficiente de variação entre as idades dos passageiros é {coeficiente_var_idades:.2f}")



print('\n- Verificando a existência de outliers inferiores -')
if len(df_titanic_idades_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_titanic_idades_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_titanic_idades_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_titanic_idades_outliers_superiores)


# Visualizando os dados sobre as Idades e os valores das tarifas
print('n\ VISUALIZANDO OS DADOS ...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle("Analise dos Dados sobre Tarifa X Idades")

# Posição 01: Gráfico das tarifas
df_titanic_tarifas_outliers_superiores_order = df_titanic_tarifas_outliers_superiores.sort_values(by='Fare',ascending=True)
plt.subplot(2,2,1)
plt.xticks([]) # Comando para remover um eixo em específico
plt.title("Lista das Tarifas")
plt.bar(df_titanic_tarifas_outliers_superiores_order["Name"],df_titanic_tarifas_outliers_superiores_order["Fare"])

# Posição 02: Gráfico das Idades
df_titanic_idades_outliers_superiores_order = df_titanic_idades_outliers_superiores.sort_values(by='Age',ascending=True)
plt.subplot(2,2,2)
plt.xticks([])
plt.title("Lista das Idades por Passageiro")
plt.barh(df_titanic_idades_outliers_superiores_order["Name"],df_titanic_idades_outliers_superiores_order["Age"])

# posição 03: Medidas descritivas das Passagens
plt.subplot(2,2,3)
plt.title('Medidas Descritivas das Tarifas')
plt.axis('off') # Comando que retira a caixa envolta do gráfico
plt.text(0.1,0.9,f'Média das Tarifas {media_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Tarifas {mediana_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Tarifas {distancia_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Tarifas {maximo_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Tarifas {minimo_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Tarifas {distancia_var_tarifa:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Tarifas {coeficiente_var_tarifa:.2f}',fontsize=12)


# posição 04: Medidas descritivas das Idades
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Empréstimos')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Idades {media_idades:.2f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Idades {mediana_idades:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Idades {distancia_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Idades {maximo_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Idades {minimo_tarifas:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Idades {distancia_var_idades:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Idades {coeficiente_var_idades:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout() # Organiza melhor os dados de exibição
plt.show()
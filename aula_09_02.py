import pandas as pd
import numpy as np

print('-------------- OBTENDO DADOS -------------')

endereco_dados = 'BASES\Titanic.csv'
df_titanic = pd.read_csv(endereco_dados, sep= ';', encoding= 'iso-8859-1')


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
df_titanic_tarifas_outliers_superiores = df_titanic[df_titanic['Fare'] > limite_superior_tarifas]
df_titanic_tarifas_outliers_inferiores = df_titanic[df_titanic['Fare'] < limite_inferior_tarifas]

df_titanic_idades_outliers_superiores = df_titanic[df_titanic['Age'] > limite_superior_idades]
df_titanic_idades_outliers_inferiores = df_titanic[df_titanic['Age'] < limite_inferior_idades]


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
print(f"O valor do Q1 - 25% das Idades é R$ {q1_idades:.2f}")
print(f"O valor do Q2 - 50% das Idades é R$ {q2_idades:.2f}")
print(f"O valor do Q3 - 75% das Idades é R$ {q3_idades:.2f}")
print(f"O valor do IQR = Q3 - Q1 das Idades é R$ {iqr_idades:.2f}")
print(f"O limite inferior das Idades é R$ {limite_inferior_idades:.2f}")
print(f"O limite superior das Idades é R$ {limite_superior_idades:.2f}")
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

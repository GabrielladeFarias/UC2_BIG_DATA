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

print('\n---------- DADOS DE EMBARQUE ----------')
print(f"A média das Tarifas é R$ {media_tarifas:.2f}")
print(f"A mediana das Tarifas é R$ {mediana_tarifas:.2f}")
print(f"A distancia entre a média e a mediana é {distancia_tarifas:.2f}%")
print(f"O maior valor das passagens  é R$ {maximo_tarifas:.2f}") 
print(f"O menor valor das passagens é R$ {minimo_tarifas:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_tarifas:.2f}")
print('\n')
print(f"A média das Idades é {media_idades:.2f}")
print(f"A mediana das Idades é {mediana_idades:.2f}")
print(f"A distancia entre a média e a mediana das idades é {distancia_idades:.2f}%")
print(f"A maior idade entre os passageiros é {maximo_idades:.2f}") 
print(f"A menor idade entre os passageiros é {minimo_idades:.2f}")
print(f"A amplitude entre as idades é {amplitude_idades:.2f}")
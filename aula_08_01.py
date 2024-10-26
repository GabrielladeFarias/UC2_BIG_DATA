import pandas as pd
import numpy as np

print('-------------- OBTENDO DADOS -------------')

endereco_dados = "BASES\Funcionarios.csv"

df_funcionarios = pd.read_csv(endereco_dados, sep= ',', encoding= 'iso-8859-1')

print('----------------- DADOS FUNCIONARIOS ------------------')
print(df_funcionarios.head())

array_salários = np.array(df_funcionarios['Salário'])
array_idades = np.array(df_funcionarios['Idade'])
array_Tempo = np.array(df_funcionarios['Tempo'])

media_idades = np.mean(array_idades)
mediana_idades = np.median(array_idades)
distancia_idades = abs((media_idades - mediana_idades) / mediana_idades)* 100

maior_idade = np.max(array_idades)
menor_idade = np.min(array_idades)
amplitude_idades = maior_idade - menor_idade


media_salarios = np.mean(array_salários)
mediana_salarios = np.median(array_salários)
distancia_salarios = abs((media_salarios - mediana_salarios) / mediana_salarios)* 100

maior_salario = np.max(array_salários)
menor_salario = np.min(array_salários)
amplitude_valores = maior_salario - menor_salario


media_tempo = np.mean(array_Tempo)
mediana_tempo = np.median(array_Tempo)
distancia_tempo = abs((media_tempo - mediana_tempo) / mediana_tempo)* 100

maior_tempo = np.max(array_Tempo)
menor_tempo = np.min(array_Tempo)
amplitude_tempo = maior_tempo - menor_tempo


print('\n --------------- DADOS SOLICITADOS -----------------')
print(F'O média salarial é R$ {media_salarios:.2f}')
print(f"A mediana dos salarios é R$ {mediana_salarios:.2f}")
print(f"A distância entre a média e a mediana é {distancia_salarios:.2f}%")
print(f"O maior valor é R$ {maior_salario:.2f}") 
print(f"O menor valor é R$ {menor_salario:.2f}")
print(f"A amplitude dos valores é R$ {amplitude_valores:.2f}")
print('\n')
print(f"A média das Idades é {media_idades:.2f}")
print(f"A mediana das Idades é {mediana_idades:.2f}")
print(f"A distancia entre a média e a mediana das idades é {distancia_idades:.2f}%")
print(f"A maior idade entre os funcionários é {maior_idade:.2f}") 
print(f"A menor idade entre os funcionários é {menor_idade:.2f}")
print(f"A amplitude entre as idades é {amplitude_idades:.2f}")
print('\n')
print(f"A média de Tempo é {media_tempo:.2f}")
print(f"A mediana de Tempo é {mediana_tempo:.2f}")
print(f"A distancia entre a média e a mediana é {distancia_tempo:.2f}%")
print(f"O maior tempo de empresa é {maior_tempo:.2f}") 
print(f"A menor tempo de empresa é {menor_tempo:.2f}")
print(f"A amplitude do tempo de empresa é {amplitude_tempo:.2f}")
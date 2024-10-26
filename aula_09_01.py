import pandas as pd
import numpy as np

print('-------------- OBTENDO DADOS --------------')

endereco_dados = 'BASES\Financeira.csv'

df_financeira = pd.read_csv(endereco_dados,sep=',', encoding='iso-8859-1')

print('\n------------ EXIBINDO A BASE DE DADOS--------------')
print(df_financeira.head())

#Obtendo Dados Sobre Renda e Valor Emprestado
array_financeira_renda = np.array(df_financeira['Renda'])
array_financeira_Vlr_emprestado = np.array(df_financeira['Vlr_emprestado'])

media_renda = np.mean(array_financeira_renda)
media_Vlr_emprestado = np.mean(array_financeira_Vlr_emprestado)

mediana_renda = np.median(array_financeira_renda)
mediana_Vlr_emprestado = np.median(array_financeira_Vlr_emprestado)

distancia_renda = abs((media_renda - mediana_renda) / mediana_renda) * 100 #Se quiser resultado percentual * 100.
distancia_Vlr_emprestado = abs((media_Vlr_emprestado - mediana_Vlr_emprestado) / mediana_Vlr_emprestado) * 100

maior_renda = np.max(array_financeira_renda)
maior_Vlr_emprestado = np.max(array_financeira_Vlr_emprestado)
menor_renda = np.min(array_financeira_renda)
menor_Vlr_emprestado = np.min(array_financeira_Vlr_emprestado)

#Obtendo a Amplitude da renda e do valor emprestado

amplitude_renda = maior_renda - menor_renda
amplitude_Vlr_empretado = maior_Vlr_emprestado - menor_Vlr_emprestado

# Obtendo os Quartis da renda e do valor emprestado

q1_renda = np.quantile(array_financeira_renda, 0.25, method='weibull') # quantile - comando para gerar quartis
q2_renda = np.quantile(array_financeira_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_financeira_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda  # Diferença entre 75% e 25% dos valores

q1_vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.25, method='weibull')
q2_vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.50, method='weibull')
q3_vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.75, method='weibull')
iqr_vlr_emprestado = q3_vlr_emprestado - q1_vlr_emprestado

#Identificando os os outliers superiores e inferiores da renda e do valor emprestado
limite_superior_renda = q3_renda + (1.5 * iqr_renda) # padrão/ (1.5 - 150%- 150/100) Utilizar sempre 50%
limite_inferior_renda = q1_renda - (1.5 * iqr_renda)

limite_superior_vlr_emprestado = q3_vlr_emprestado + (1.5 * iqr_vlr_emprestado) # padrão/ (1.5 - 150%- 150/100) Utilizar sempre 50%
limite_inferior_vlr_emprestado = q1_vlr_emprestado - (1.5 * iqr_vlr_emprestado)

# Filtrando o DataFrame Financeira
df_financeira_renda_outliers_superiores = df_financeira[df_financeira['Renda'] > limite_superior_renda] #Todos os valores maiores que o limite superior
df_financeira_renda_outliers_inferiores = df_financeira[df_financeira['Renda'] < limite_inferior_renda]

df_financeira_vlr_outliers_superiores = df_financeira[df_financeira['Vlr_emprestado'] > limite_superior_vlr_emprestado] #Todos os valores maiores que o limite superior
df_financeira_vlr_outliers_inferiores = df_financeira[df_financeira['Vlr_emprestado'] < limite_inferior_vlr_emprestado]

print('\n-------- OBTENDO INFORMAÇÕES SOBRE RENDA ---------')
print(f"A média das rendas dos clientes é R$ {media_renda:.2f}")
print(f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}")
print(f"A distancia entre a média e a mediana das rendas dos clientes é {distancia_renda:.2f}%")
print(f"O maior valor das rendas dos clientes é R${maior_renda}") 
print(f"O menor valor das rendas dos clientes é R${menor_renda}")
print(f"A amplitude das vendas od clientes é R${amplitude_renda}")
print('\n---------- Medidas de Tendência Central -----------')
print(f"O valor do Q1 - 25% da renda é R$ {q1_renda:.2f}")
print(f"O valor do Q2 - 50% da renda é R$ {q2_renda:.2f}")
print(f"O valor do Q3 - 75% da renda é R$ {q3_renda:.2f}")
print(f"O valor do IQR = Q3 - Q1 da renda é R$ {iqr_renda:.2f}")
print(f"O limite inferior da renda é R$ {limite_inferior_renda:.2f}")
print(f"O limite superior da renda é R$ {limite_superior_renda:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_financeira_renda_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_renda_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_financeira_renda_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_renda_outliers_superiores)

print('\n-------- OBTENDO INFORMAÇÕES SOBRE EMPRÉSTIMO ---------')
print(f"A média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}")
print(f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}")
print(f"A distancia entre a média e a mediana dos empréstimos dos clientes é  {distancia_Vlr_emprestado:.2f}%")
print(f"O maior valor dos empréstimos dos clientes é R${maior_Vlr_emprestado:.2f}")
print(f"O menor valor dos empréstimos dos clientes é R${menor_Vlr_emprestado:.2f}")
print(f"A amplitude dos empréstimos dos clientes é R${amplitude_Vlr_empretado:.2f}")
print('\n---------- Medidas de Tendência Central -----------')
print(f"O valor do Q1 - 25% dos empréstimos  é R$ {q1_vlr_emprestado:.2f}")
print(f"O valor do Q2 - 50% dos empréstimos é R$ {q2_vlr_emprestado:.2f}")
print(f"O valor do Q3 - 75% dos empréstimos é R$ {q3_vlr_emprestado:.2f}")
print(f"O valor do IQR = Q3 - Q1 dos empréstimos é R$ {iqr_vlr_emprestado:.2f}")
print(f"O limite inferior dos empréstimos é R$ {limite_inferior_vlr_emprestado:.2f}")
print(f"O limite superior dos empréstimos é R$ {limite_superior_vlr_emprestado:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_financeira_vlr_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_vlr_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_financeira_vlr_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_vlr_outliers_superiores)
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

amplitude_renda = maior_renda - menor_renda
amplitude_Vlr_empretado = maior_Vlr_emprestado - menor_Vlr_emprestado

print('\n-------- OBTENDO INFORMAÇÕES SOBRE RENDA ---------')
print(f"A média das rendas dos clientes é R$ {media_renda:.2f}")
print(f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}")
print(f"A distancia entre a média e a mediana das rendas dos clientes é {distancia_renda:.2f}%")
print(f"O maior valor das rendas dos clientes é R${maior_renda}") 
print(f"O menor valor das rendas dos clientes é R${menor_renda}")
print(f"A amplitude das vendas od clientes é R${amplitude_renda}")

      
print('\n-------- OBTENDO INFORMAÇÕES SOBRE EMPRÉSTIMO ---------')
print(f"A média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}")
print(f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}")
print(f"A distancia entre a média e a mediana dos empréstimos dos clientes é  {distancia_Vlr_emprestado:.2f}%")
print(f"O maior valor dos empréstimos dos clientes é R${maior_Vlr_emprestado:.2f}")
print(f"O menor valor dos empréstimos dos clientes é R${menor_Vlr_emprestado:.2f}")
print(f"A amplitude dos emréstimos dos clientes é R${amplitude_Vlr_empretado:.2f}")
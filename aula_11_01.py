import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('-------------- OBTENDO DADOS -------------')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df_ocorrencias = pd.read_csv(endereco_dados, sep= ';', encoding= 'iso-8859-1')
df_roubo_veiculos = df_ocorrencias[['munic','roubo_veiculo','cisp']]
df_roubo_veiculos = df_roubo_veiculos.groupby(['cisp']).sum(['roubo_veiculo']).reset_index() #(groupby) agrupa os dados.

print('\n-------------- OBTENDO DADOS GERAIS DE OCORRÊNCIAS ------------')
print(df_ocorrencias.head())
print(df_roubo_veiculos.head())

array_roubo_veiculos = np.array(df_roubo_veiculos['roubo_veiculo']) #após o array, usar o (df) que tem os filtros

media_roubos = np.mean(array_roubo_veiculos)
mediana_roubos = np.median(array_roubo_veiculos)
distancia_roubos = abs((media_roubos - mediana_roubos) / mediana_roubos)* 100

maximo_roubos = np.max(array_roubo_veiculos)
minimo_roubos = np.min(array_roubo_veiculos)
amplitude_roubos = maximo_roubos - minimo_roubos

q1_roubos = np.quantile(array_roubo_veiculos, 0.25, method='weibull') 
q2_roubos = np.quantile(array_roubo_veiculos, 0.50, method='weibull')
q3_roubos = np.quantile(array_roubo_veiculos, 0.75, method='weibull')
iqr_roubos = q3_roubos - q1_roubos  

limite_superior_roubos = q3_roubos + (1.5 * iqr_roubos)
limite_inferior_roubos = q1_roubos - (1.5 * iqr_roubos)

df_ocorrencias_roubos_outliers_superiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] > limite_superior_roubos]
df_ocorrencias_roubos_outliers_inferiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] < limite_inferior_roubos]

variancia_roubos = np.var(array_roubo_veiculos)
distancia_var_roubos = variancia_roubos / (media_roubos**2) #Fórmula matemática para calcular a distancia
desvio_padrao_roubos = np.std(array_roubo_veiculos)
coeficiente_var_roubos = desvio_padrao_roubos / media_roubos

print('\n---------- OBTENDO INFORMAÇÕES SOBRE ROUBOS DE AUTOMÓVEIS ----------')
print(f"A média dos Roubos a Veículos é  {media_roubos:.2f}")
print(f"A mediana dos Roubos a Veículos  {mediana_roubos:.2f}")
print(f"A distancia entre a média e a mediana é {distancia_roubos:.2f} %")
print(f"O maior valor dos Roubos a Veículos  é  {maximo_roubos:.2f}") 
print(f"O menor valor dos Roubos a Veículos é  {minimo_roubos:.2f}")
print(f"A amplitude dos valores dos Roubo a Veículos é {amplitude_roubos:.2f}")
print('\n')

print('\n---------- Medidas de Tendência Central -----------')
print(f"O valor do Q1 - 25% dos Roubos é  {q1_roubos:.2f}")
print(f"O valor do Q2 - 50% dos Roubos é  {q2_roubos:.2f}")
print(f"O valor do Q3 - 75% dos Roubos é  {q3_roubos:.2f}")
print(f"O valor do IQR = Q3 - Q1 dos Roubos é  {iqr_roubos:.2f}")
print(f"O limite inferior dos Roubos é {limite_inferior_roubos:.2f}")
print(f"O limite superior dos Roubos é {limite_superior_roubos:.2f}")
print(f"A variância dos Roubos é {variancia_roubos:.2f}")
print(f"A distância da variância X média dos Roubos é {distancia_var_roubos:.2f} %")
print(f"O desvio padrão dos Roubos é {desvio_padrao_roubos:.2f}")
print(f"O coeficiente de variação dos Roubos é {coeficiente_var_roubos:.2f}")


print('\n- Verificando a existência de outliers inferiores -')
if len(df_ocorrencias_roubos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_ocorrencias_roubos_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_ocorrencias_roubos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_ocorrencias_roubos_outliers_superiores)


print('n\ VISUALIZANDO OS DADOS ...')
plt.subplots(2,2,figsize=(12,7))
plt.suptitle("Analise dos Roubos a Veículos")

# Posição 01: Gráfico das tarifas
plt.subplot(2,2,1)
df_ocorrencias_roubos_outliers_superiores_order = df_ocorrencias_roubos_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.title("Lista de Roubos a Veículos por Delegacia")
plt.barh(df_ocorrencias_roubos_outliers_superiores_order["cisp"].astype(str),df_ocorrencias_roubos_outliers_superiores_order["roubo_veiculo"])


plt.subplot(2,2,3)
plt.title('Medidas Descritivas de Roubo a Veículos')
plt.axis('off')
plt.text(0.1,0.8,f'Média dos Roubos {media_roubos:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Mediana dos Roubos {mediana_roubos:.2f}',fontsize=12)
plt.text(0.1,0.6,f'Distância entre Média e Mediana das Tarifas {distancia_roubos:.2f} %',fontsize=12)
plt.text(0.1,0.5,f'Maior valor dos Roubos {maximo_roubos:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Menor valor dos Roubos {minimo_roubos:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Distância entre a Variância e Média dos Roubos {distancia_var_roubos:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Coeficiente de variação dos Roubos {coeficiente_var_roubos:.2f}',fontsize=12)

plt.subplot(2,2,2)
plt.axis('off')

plt.subplot(2,2,4)
plt.axis('off')

plt.tight_layout() # Organiza melhor os dados de exibição
plt.show()
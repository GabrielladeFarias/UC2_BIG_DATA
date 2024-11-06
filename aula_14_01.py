import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_lesao_corp_dolosa = df_ocorrencias[['cisp','ano','lesao_corp_dolosa']]
df_lesao_corp_dolosa = df_lesao_corp_dolosa[df_lesao_corp_dolosa['ano'].isin([2022,2023,2024])] #O filtro deve ser aplicado antes do agrupamento. (isin)
df_lesao_corp_dolosa = df_lesao_corp_dolosa.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index() #Agrupameno (groupby)


df_lesao_doloso_culposo = df_ocorrencias[['cisp','ano','lesao_corp_dolosa','lesao_corp_culposa']]
df_lesao_doloso_culposo = df_lesao_doloso_culposo[df_lesao_doloso_culposo['ano'].isin([2022,2023,2024])] #O filtro deve ser aplicado antes do agrupamento.
df_lesao_doloso_culposo = df_lesao_doloso_culposo.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_culposa']).reset_index()

print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesao_corp_dolosa.head()) # O comando head apresenta as 5 primeiras posição, mas é possível mudar. ex: head(10)

# Criando o array dos roubos de veiculos
array_lesao_dolosa = np.array(df_lesao_corp_dolosa["lesao_corp_dolosa"])

# Obtendo a média dos roubos de veiculos
media_lesao_dolosa = np.mean(array_lesao_dolosa)

# Obtendo a mediana dos roubos de veiculos
mediana_lesao_dolosa = np.median(array_lesao_dolosa)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_lesao_dolosa = abs((media_lesao_dolosa - mediana_lesao_dolosa) / mediana_lesao_dolosa) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_lesao_dolosa = np.max(array_lesao_dolosa)
minimo_lesao_dolosa = np.min(array_lesao_dolosa)

# Obtendo a amplitude dos roubos de veiculos
amplitude_lesao_dolosa = maximo_lesao_dolosa - minimo_lesao_dolosa

q1_lesao_dolosa = np.quantile(array_lesao_dolosa, 0.25, method='weibull')
q2_lesao_dolosa = np.quantile(array_lesao_dolosa, 0.50, method='weibull')
q3_lesao_dolosa = np.quantile(array_lesao_dolosa, 0.75, method='weibull')
iqr_lesao_dolosa = q3_lesao_dolosa - q1_lesao_dolosa

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_lesao_dolosa = q3_lesao_dolosa + (1.5 * iqr_lesao_dolosa)
limite_inferior_lesao_dolosa = q1_lesao_dolosa - (1.5 * iqr_lesao_dolosa)

# Filtrando o DataFrame roubos de veículos
df_lesao_dolosa_outliers_superiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_dolosa]
df_lesao_dolosa_outliers_inferiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] < limite_inferior_lesao_dolosa]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_lesao_dolosa = np.var(array_lesao_dolosa)
distancia_var_lesao_dolosa = variancia_lesao_dolosa / (media_lesao_dolosa**2)
desvio_padrao_lesao_dolosa = np.std(array_lesao_dolosa)
coeficiente_var_lesao_dolosa = desvio_padrao_lesao_dolosa / media_lesao_dolosa

correlacao_lesao = np.corrcoef(df_lesao_doloso_culposo['lesao_corp_dolosa'],df_lesao_doloso_culposo['lesao_corp_culposa'])[0,1]

print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS HOMICÍDIOS DOLOSOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das Lesões Corporais Dolosas é {media_lesao_dolosa:.0f}")
print(f"A mediana das Lesões Corporais Dolosas é {mediana_lesao_dolosa:.0f}")
print(f"A distância entre a média e a mediana é das Lesões Corporais Dolosas é {distancia_lesao_dolosa:.2f} %")
print(f"O menor valor das Lesões Corporais Dolosas é {minimo_lesao_dolosa:.0f}")
print(f"O maior valor das Lesões Corporais Dolosas é {maximo_lesao_dolosa:.0f}")
print(f"A amplitude dos valores das Lesões Corporais Dolosas é {amplitude_lesao_dolosa:.0f}")
print(f"O valor do q1 - 25% das Lesões Corporais Dolosas é {q1_lesao_dolosa:.0f}")
print(f"O valor do q2 - 50% das Lesões Corporais Dolosas é {q2_lesao_dolosa:.0f}")
print(f"O valor do q3 - 75% das Lesões Corporais Dolosas é {q3_lesao_dolosa:.0f}")
print(f"O valor do iqr = q3 - q1 das Lesões Corporais Dolosas é {iqr_lesao_dolosa:.0f}")
print(f"O limite inferior das Lesões Corporais Dolosas é {limite_inferior_lesao_dolosa:.0f}")
print(f"O limite superior das Lesões Corporais Dolosas é {limite_superior_lesao_dolosa:.0f}")
print(f"A variância das Lesões Corporais Dolosas é {variancia_lesao_dolosa:.0f}")
print(f"A distância da variância X média das Lesões Corporais Dolosas é {distancia_var_lesao_dolosa:.0f}")
print(f"O desvio padrão das Lesões Corporais Dolosas é {desvio_padrao_lesao_dolosa:.0f}")
print(f"O coeficiente de variação das Lesões Corporais Dolosas é {coeficiente_var_lesao_dolosa:.0f}")
print(f"A correlação das Lesões Corporais Dolosas e Culposas é {correlacao_lesao:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_lesao_dolosa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesao_dolosa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_lesao_dolosa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_lesao_dolosa_outliers_superiores)

print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7)) # O primeiro número se refere a linha e o segundo as colunas/ figsize= (tamanho da tela)
plt.suptitle('Análise dos Dados sobre Lesões Corporais Dolosas')

plt.subplot(2,2,1)
plt.title('BoxPlot das Lesões Corporais Dolosas')
plt.boxplot(array_lesao_dolosa,vert=False,showmeans=True)

plt.subplot(2,2,2)
plt.title('Comparativo Lesões Corporais Dolosas e Culposas')
plt.scatter(df_lesao_doloso_culposo['lesao_corp_dolosa'],df_lesao_doloso_culposo['lesao_corp_culposa'])
plt.xlabel('Lesão Corporal Dolosa')
plt.ylabel('Lesão Corporal Culposa')

plt.subplot(2,2,3)
df_lesao_dolosa_outliers_superiores_order = df_lesao_dolosa_outliers_superiores.sort_values(by='lesao_corp_dolosa',ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_lesao_dolosa_outliers_superiores_order['cisp'].astype(str),df_lesao_dolosa_outliers_superiores['lesao_corp_dolosa'].sort_values(), color= 'pink', edgecolor= 'red')



plt.subplot(2,2,4)
plt.title('Medidas Descritivas das Lesões Corporais Dolosas')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Lesões Corporais Dolosas: {media_lesao_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Lesões Corporais Dolosas: {mediana_lesao_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Lesões Corporais Dolosas: {distancia_lesao_dolosa:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Lesões Corporais Dolosas: {maximo_lesao_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Lesões Corporais Dolosas: {minimo_lesao_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Lesões Corporais Dolosas: {distancia_var_lesao_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Lesões Corporais Dolosas: {coeficiente_var_lesao_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre as Lesões Corporais Dolosas e Culposas: {correlacao_lesao:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
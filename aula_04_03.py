import pandas as pd

def formatar(valor):
  return  "{:.2f}%".format(valor)

municipios = [
    ['Rio de Janeiro',6775561,35000],
    ['Niterói',515317,2500],
    ['São Gonçalo',1091737,15000],
    ['Duque de Caxias',914624,12000],
    ['Nova Iguaçu',821128,10000],
    ['Belford Roxo',513118,9000],
    ['São João de Meriti',472906,8500],
    ['Petrópolis',306678,1000],
    ['Volta Redonda',273988,2000],
    ['Campos dos Goytacazes',507548,4000],
]

colunas = ['Município','Hábitantes','Roubos']

df_municipios = pd.DataFrame(municipios,columns=colunas)

print("\n-------------- Tabela Municípios ---------------")
print(df_municipios)

soma_roubos = df_municipios['Roubos'].sum(axis=0)
media_roubos = df_municipios['Roubos'].mean(axis=0)

soma_populacao = df_municipios['Hábitantes'].sum(axis=0)
media_populacao = df_municipios['Hábitantes'].mean(axis=0)

maior_roubos = df_municipios['Roubos'].max(axis=0)
menor_roubos = df_municipios['Roubos'].min(axis=0)

maior_populacao = df_municipios['Hábitantes'].max(axis=0)
menor_populacao = df_municipios['Hábitantes'].min(axis=0)

maior_municipio_roubos = df_municipios[df_municipios['Roubos'] == maior_roubos]['Município']
menor_municipio_roubos = df_municipios[df_municipios['Roubos'] == menor_roubos]['Município']

maior_municipio_populacao = df_municipios[df_municipios['Hábitantes'] == maior_populacao]['Município']
menor_municipio_populacao = df_municipios[df_municipios['Hábitantes'] == menor_populacao]['Município']

#tx_roubos = ((df_municipios['Roubos']/df_municipios['Hábitantes'])*100).apply(formatar)
df_municipios['Taxa'] = ((df_municipios['Roubos'] / df_municipios['Hábitantes'])*100).apply(formatar)


print("\n-------------- Informações Solicitadas ----------------")
print(f"A quantidade total de roubos no período foi {soma_roubos}")
print(f"A quantidade média de roubos no período foi {media_roubos:.0f}")
print(f"A quantidade total de habitantes no período foi {soma_populacao}")
print(f"A quantidade média de habitantes no período foi {media_populacao:.0f}")
print(f"O maior valor de roubos no período foi {maior_roubos}.")
print(f"O maior valor de roubos no período foi {menor_roubos}.")
print(f"O município com mais roubos foi {maior_municipio_roubos.values[0]}.")
print(f"O município com menos roubos foi {menor_municipio_roubos.values[0]}.")
print(f"O maior valor populacional no Estado é {maior_municipio_populacao.values[0]}.")
print(f"O maior valor populacional no Estado é {menor_municipio_populacao.values[0]}.")

print("\n---- Taxa de Roubos ----")
print(df_municipios[['Município','Taxa']])
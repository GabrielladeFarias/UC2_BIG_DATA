import pandas as pd

dados_vendedores = [
    ['Ana','F',28,120],
    ['Bruno','M',34,150],
    ['Carlos','M',45,110],
    ['Diana','F',30,95],
    ['Eduardo','M',40,130],
    ['Fernanda','F',29,140],
    ['Gustavo','M',38,105],
    ['Helena','F',31,125],
    ['Igor','M',27,100],
    ['Juliana','F',33,135]
]
colunas = ['Nome','Sexo','Idade','Qtd_Vendas']

df_dados_vendedores = pd.DataFrame(dados_vendedores,columns=colunas)

print("\n-- Tabela Dados dos Vendedores --")
print(df_dados_vendedores)

#Calculo das Vendas
soma_vendas = df_dados_vendedores['Qtd_Vendas'].sum(axis=0)
media_vendas = df_dados_vendedores['Qtd_Vendas'].mean(axis=0)
maior_venda = df_dados_vendedores['Qtd_Vendas'].max(axis=0)
menor_venda = df_dados_vendedores['Qtd_Vendas'].min(axis=0)
maior_venda_nome = df_dados_vendedores[df_dados_vendedores['Qtd_Vendas'] == maior_venda]['Nome']
menor_venda_nome = df_dados_vendedores[df_dados_vendedores['Qtd_Vendas'] == menor_venda]['Nome']

#Calculodas Idades
media_idade = df_dados_vendedores['Idade'].mean(axis=0)
maior_idade = df_dados_vendedores['Idade'].max(axis=0)
menor_idade = df_dados_vendedores['Idade'].min(axis=0)

# Calculo das Vendas por Sexo
vendas_sexo_f = df_dados_vendedores[df_dados_vendedores['Sexo'] == 'F']['Qtd_Vendas'].sum(axis=0)
vendas_sexo_m = df_dados_vendedores[df_dados_vendedores['Sexo'] == 'M']['Qtd_Vendas'].sum(axis=0)

print("\n---- Informações Solicitadas ----")
print(f"A quantidade total de vendas no período foi {soma_vendas}")
print(f"A quantidade média de vendas no período foi {media_vendas:.0f}")
print(f"A média das idades dos vendedores é {media_idade:.0f} anos.")
print(f"A maior das idades dos vendedores é {maior_idade} anos.")
print(f"A menor das idades dos vendedores é {menor_idade} anos.")
print(f"O nome do vendedor com mais vendas é {maior_venda_nome.values[0]}")
print(f"O nome do vendedor com menos vendas é {menor_venda_nome.values[0]}")
print(f"A quantidade de vendas do sexo masculino foi {vendas_sexo_m}")
print(f"A quantidade de vendas do sexo feminino foi {vendas_sexo_f}")
# EXERCÍCIOS
import pandas as pd
#Importando a base de Dados
endereco_dados = "BASES\Funcionarios.csv"
#Importando o DataFrame                                          #O iso para oBrasil é sempre o mesmo.
df_funcionarios = pd.read_csv(endereco_dados, sep= ',', encoding= 'iso-8859-1') #sempre verificar o (sep=) - separador. Pode ser (,) (;) (/)

#Exibindo os Dados do DataFrame
print('----------------- DADOS FUNCIONARIOS ------------------')
print(df_funcionarios.head())

media_salarial = df_funcionarios['Salário'].mean(axis=0)
media_idade = df_funcionarios['Idade'].mean(axis=0)


maior_tempo = df_funcionarios['Tempo'].max(axis=0)
menor_tempo = df_funcionarios['Tempo'].min(axis=0)
func_tempo_velho = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
func_tempo_novo = df_funcionarios[df_funcionarios['Tempo'] == menor_tempo]['Nome']
diferenca_tempo = maior_tempo - menor_tempo

media_tempo = df_funcionarios['Tempo'].mean(axis=0)

maior_idade = df_funcionarios['Idade'].max(axis=0)
menor_idade = df_funcionarios['Idade'].min(axis=0)
maior_idade_func = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']
menor_idade_func = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
diferenca_idade = maior_idade - menor_idade

qtd_func = df_funcionarios['Nome'].count()

maior_salario = df_funcionarios['Salário'].max(axis=0)
func_sal_maior = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']

print('\n --------------- DADOS SOLICITADOS -----------------')
print(F'O salário médio da empresa é R${media_salarial:.2f}')
print(f'A Média das Idades dos Funcionários é {media_idade:.0f} anos')
print(f'O Maior Tempo de Empresa é {maior_tempo} anos')
print(f'O Menor Tempo de Empresa é {menor_tempo} anos')
print(f"O(A) Funcionário(a) mais novo(a) na empresa é {func_tempo_novo.to_string(index=False)}")
print(f"O(A) Funcionário(a) mais antigo(a) na empresa é {func_tempo_velho.to_string(index=False)}")
print(f'A Diferença de tempo de empresa é {diferenca_tempo}')

print(f'A Média do Tempo de Casa é {media_tempo:.0f}')

print(f"O Funcionário mais velho é  {maior_idade_func.to_string(index=False)}")
print(f"O Funcionário mais novo é {menor_idade_func.to_string(index=False)}")

print(f'A Quantidade de funcionários na empresa é {qtd_func}')
print(f"O(A) Funcionário(a) com maior salário é {func_sal_maior.to_string(index=False)}")
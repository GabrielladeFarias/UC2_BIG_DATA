import pandas as pd
#Importando a base de Dados
endereco_dados = "BASES\Financeira.csv"
#Importando o DataFrame                                          #O iso para oBrasil é sempre o mesmo.
df_financeira = pd.read_csv(endereco_dados, sep= ',', encoding= 'iso-8859-1') #sempre verificar o (sep=) - separador. Pode ser (,) (;) (/)

#Exibindo os Dados do DataFrame
print('------ DADOS FINANCEIROS ------')
print(df_financeira.head())
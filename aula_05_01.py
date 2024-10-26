#pip install xlrd - Biblioteca para manipular arquivos xlsx
#pip install openpyxl - BiBLIOTECA PARA MANIPULAR ARQUIVOS NO EXCEL

import pandas as pd
#Importando a Base de Dados
endereco_dados = 'BASES\ENEM_2020_2023.xlsx'
#Criando o DataFrame
df_enem = pd.read_excel(endereco_dados)
#Exibindo os Dados do DataFrame
print('-- QUANTIDADE DE INSCRITOS NO ENEM 2020 A 2023 --')
print(df_enem.head())
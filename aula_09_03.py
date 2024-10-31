import pandas as pd
import numpy as np

print('-------------- OBTENDO DADOS -------------')

endereco_dados = 'BASES\ENEM_2020_2023 (1).xlsx'
df_enem = pd.read_excel(endereco_dados)

print('-- QUANTIDADE DE INSCRITOS NO ENEM 2020 A 2023 --')
print(df_enem.head())
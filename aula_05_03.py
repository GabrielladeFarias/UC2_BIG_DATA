import pandas as pd

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' # Importando dados via web / sempre que o arquivo fo atualizado será renovado aqui.

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

print(df_ocorrencias.head())


import pandas as pd

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
print('\n--------- OBTENDO DADOS GERAIS SOBRE OCORRENCIAS')
print(df_ocorrencias.head())

#Criando DataFrame sobre Roubo de Veículos por Município
df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
print('\n---------- OBTENDO DADOS SOBRE ROUBOS DE VEÍCULOS ----------')
print(df_roubo_veiculo.head())

# Criando DataFrame sobre Homicídio Doloso por Ano
df_ano_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
df_ano_hom_doloso = df_ano_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()

print('\n----------- OBTENDO DADOS SOBRE HOMICÍDIO DOLOSO-----------')
print(df_ano_hom_doloso.head())
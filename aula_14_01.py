import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['cisp','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['cisp']).sum(['hom_doloso']).reset_index()
df_rec_veiculo = df_rec_veiculo[df_rec_veiculo['ano'].isin([2022,2023])]


df_rec_veiculo_ano = df_ocorrencias[['aisp','ano','recuperacao_veiculo']]
df_rec_veiculo_ano = df_rec_veiculo_ano.groupby(['ano']).sum(['recuperacao_veiculos']).reset_index()
df_hom_doloso_culposo = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_hom_doloso_culposo = df_hom_doloso_culposo.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()


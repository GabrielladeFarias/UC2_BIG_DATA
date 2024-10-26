import pandas as pd
def formatar(valor):
  return "R${:.2f}".format(valor)
maria = pd.Series([800,700,1000,900,1200,600,600])
joao = pd.Series([900,500,1100,1000,900,500,700])
manuel = pd.Series([700,600,900,1200,900,700,400])
print("\n--------------- Dados Vendas -----------------")
print("VENDEDOR  MÉDIA   MAIOR_VALOR  MENOR_VALOR")
print(f"MARIA:  R${maria.mean():.2F} - R${maria.max():.2F} - R${maria.min():.2F}")
print(f"JOÃO:   R${joao.mean():.2F} - R${joao.max():.2F} - R${joao.min():.2F}")
print(f"MANUEL: R${manuel.mean():.2F} - R${manuel.max():.2F} - R${manuel.min():.2F}")
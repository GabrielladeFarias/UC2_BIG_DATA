import pandas as pd
def formatar(valor):
  return "{:.2f}%".format(valor)
roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
recuperacao = pd.Series([70,50,90,80,100,70,50])
roubo_furto = roubo + furto
taxa_rec = ((recuperacao/roubo_furto) * 100).apply(formatar)
print("\n- Total Geral de Roubos -")
print(f"{roubo_furto.sum()}")
print("\n- Total de Roubos Diários -")
print(f"{roubo_furto}")
print("\n- Taxa de Recuperação Diária -")
print(f"{taxa_rec}")
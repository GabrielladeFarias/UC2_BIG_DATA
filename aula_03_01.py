import pandas as pd
qtd_vac = pd.Series([30000000, 25000000, 10000000, 5000000])
qtd_pop = pd.Series([213317639, 214477744, 215574303, 216687971])
soma1 = qtd_vac.sum()
media_pop_vac = qtd_vac.mean()
soma2 = qtd_pop.sum()
media_pop_br = qtd_pop.mean()
taxa_vac = qtd_vac/qtd_pop
print(f"Nos últimos quatro anos o total de pessoas vacinadas foi {soma1} e sua média {media_pop_vac}.")
print(f"O total e média da população do Brasil no periodo de quatro anos foi {soma2}, {media_pop_br}.")
print(f"A taxa de vacinação anual dos últimos quatro anos foi: {taxa_vac}")
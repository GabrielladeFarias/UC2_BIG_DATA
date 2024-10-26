# Código usando séries
import pandas as pd
media = pd.Series([80,90,10,20,30,40,70,100,30,50])
ap = media[media >=70]
rp = media[media <=70]
print("Médias maiores que 70")
print(ap)
print("Médias menores que 70")
print(rp)
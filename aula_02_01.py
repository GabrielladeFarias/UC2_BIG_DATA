# Código usando listas
media = [80,90,10,20,30,40,70,100,30,50]
ap = []
rp = []
for i in range(len(media)):
    if media[i] >= 70:
        ap.append(media[i])
    else:
        rp.append(media[i])
print(ap)
print(rp)
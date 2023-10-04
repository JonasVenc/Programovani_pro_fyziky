soucet = 0
prvni_clen = int(input("Zadejte první člen posloupnosti: "))
posledni_clen = int(input("Zadejte poslední člen posloupnosti: "))
i = 1

while i < posledni_clen + 1:
    soucet = soucet + prvni_clen - 1 + i
    i+=1



print("Součet řady cyklem: ", soucet)

soucet = 0

pocet_clenu = posledni_clen - prvni_clen +1
soucet = int(pocet_clenu * (prvni_clen + posledni_clen) / 2)

print("Soucet řady vzorcem: ", soucet)

wait = input("\nStiskem libovolné klávesy se program ukončí...")
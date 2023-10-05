soucet = 0
prvni_clen = int(input("Zadejte první člen posloupnosti: "))
posledni_clen = int(input("Zadejte poslední člen posloupnosti: "))

for i in range(prvni_clen, posledni_clen+1):
    soucet = soucet + i

print("Součet řady cyklem: ", soucet)

soucet = 0

pocet_clenu = posledni_clen - prvni_clen +1
soucet = int(pocet_clenu * (prvni_clen + posledni_clen) / 2)

print("Soucet řady vzorcem: ", soucet)

wait = input("\nStiskem libovolné klávesy se program ukončí...")
# Python: Eratosthenovo síto pro nalezení všech prvočísel menších než nebo rovných nmax
from numba import njit
import numpy as np

# vrací integer numpy pole prvočísel od 2 do nmax včetně
@njit
def sieve_of_eratosthenes(nmax):
  a=np.full(nmax+1,True)       # alokace dynamického pole bool prvků (zde: síto)
  a[0:2]=False                 # 0 a 1 nejsou prvočísla
  n=2                          # první prvočíslo
  while n<=np.sqrt(nmax):      # průchod od 2 do sqrt(nmax)
    nn=n*n                     # nejbližší nevyškrtnutý násobek
    while nn<=nmax:            # vyškrtávání násobků
      a[nn]=False              # - všech
    # if a[nn]: a[nn]=False    # - jen dosud nevyškrtnutých
      nn+=n                    # posun na další násobek
    while True:                # posun na další nevyškrtnutý prvek
      n+=1
      if a[n]: break           # skok z vnitřního cyklu na začátek vnějšího cyklu
  cnt=0
  for n in range(nmax+1):      # zjištění počtu nevyškrtnutých prvků
    if a[n]: cnt+=1
  # cnt=sum(1 for _ in a if _) # alternativa neschůdná pro Numbu
  result=np.zeros(cnt,dtype=np.int32)  # alokace výstupního pole prvočísel
  nprime=0
  for n in range(nmax+1):      # průchod sítem
    if a[n]:
      result[nprime]=n         # přenos prvočísel z indexů v sítu do výstupního pole
      nprime+=1
  return result


#nmax=1_000
# nmax=1_000_000_000
N=1_000_000_000

filename='primes.bin'                  # jméno souboru
f=open(filename,'wb')                    # otevření textového souboru pro zápis

filename2='twins.bin'                  # jméno souboru
fi=open(filename2,'wb')                    # otevření textového souboru pro zápis

for nmax in range(N):
  prvocisla=sieve_of_eratosthenes(nmax)
  #for n in range(len(prvocisla)): print(f'{prvocisla[n]:8d}',file=f) # zápis prvočísel do souboru
  #print()
  #print('Pocet prvocisel mensich nez nebo rovnych '+str(nmax)+':',len(prvocisla))
  prvocisla_len = len(prvocisla)

  f.write(prvocisla_len.to_bytes(4, byteorder='big'))

  #dvojcata=np.empty(nmax,dtype=int)
  k=0
  for i in range(prvocisla_len):
      if i + 1 < prvocisla_len:
          if prvocisla[i] + 2 == prvocisla[i + 1]:
              #print(f'{prvocisla[i]:8d}',file=f) # zápis prvočísel do souboru
              #dvojcata[k] = prvocisla[i]
              k += 1
              #print(prvocisla[i])
          else:
              if i + 2 < prvocisla_len:
                  if prvocisla[i] + 2 == prvocisla[i + 2]:
                      #print(f'{prvocisla[i]:8d}',file=f) # zápis prvočísel do souboru
                      #dvojcata[k] = prvocisla[i]
                      k += 1
                      #print(prvocisla[i])
  fi.write(k.to_bytes(4, byteorder='big'))

f.close()                               # uzavření souboru
fi.close()                               # uzavření souboru
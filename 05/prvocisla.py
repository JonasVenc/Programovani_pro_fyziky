# Python: Eratosthenovo síto pro nalezení všech prvočísel menších než nebo rovných nmax
from numba import njit
import numpy as np
import matplotlib.pyplot as plt

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

@njit
def dvojice(prvocisla, delka):
  pocet = 0
  for i in range (delka - 1):
    if prvocisla[i+1] - prvocisla[i] == 2:
      pocet += 1
  return pocet

#nmax=1_000
# nmax=1_000_000_000
N=1_000_000_000

prvocisla = sieve_of_eratosthenes(N)
dvojcata = dvojice(prvocisla, len(prvocisla))

print("pocet prvocisel mensich nebo rovnych je: "+str(N) + ":" + str(len(prvocisla)))
print("pocet dvojiciek je: " + str(dvojcata))

filename='primes.dat'                  # jméno souboru
f=open(filename,'w')                    # otevření textového souboru pro zápis
for n in range(len(prvocisla)): print(f"{prvocisla[n]:8d}", file = f)
f.close()

n = np.arange(2, 100000001, 1000000)
prvocisla_poc = []
dvojcata_poc = []

for a in n:
  primes = sieve_of_eratosthenes(a)
  twin_primes = dvojice(primes, len(primes))
  prvocisla_poc.append(len(primes))
  dvojcata_poc.append(twin_primes)


plt.plot(n, prvocisla_poc, label = "prvocisla")
plt.plot(n, dvojcata_poc, label = "dvojicky")
plt.legend()
plt.show()
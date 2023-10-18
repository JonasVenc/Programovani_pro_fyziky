from mPi_fast import pi, piMachin, piLeibniz, piEuler, piViete, piRamanujan

format='%25s%20.15f'
nmax=1_000_000

print(format % ('pi podle math =', pi))
print(format % ('pi podle Machina =', piMachin()))
print(format % ('pi podle Leibnize =', piLeibniz(nmax)))
print(format % ('pi podle Euler =', piEuler(nmax)))
print(format % ('pi podle Vieta =', piViete(nmax)))
print(format % ('pi podle Ramanujana =', piRamanujan(nmax)))
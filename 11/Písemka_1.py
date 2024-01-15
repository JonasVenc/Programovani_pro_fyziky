import numpy as np

def integral(a, b, p, q, m):
    if m == 0:
        return p*(np.cos(a) - np.cos(b)) + q*(np.sin(b) - np.sin(a))
    else:
        return (integral(a, b, -q, p, m-1)*m + a**m*(p*np.cos(a) - q*np.sin(a)) - b**m*(p*np.cos(b) - q*np.sin(b)))
    
print(integral(0, np.pi/2, 1, -2, 6))
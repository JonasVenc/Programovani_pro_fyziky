import numpy as np

cara1 = np.array([[[6, 6], [10, 5]],   [[6, 4], [5, 0]],
                  [[4, 6], [5, 10]],   [[10,5], [6, 4]],
                  [[4, 6], [0,  5]],   [[5,10], [6, 6]],
                  [[4, 4], [0,  5]],   [[4, 4], [5, 0]]])

x = []

for i in range (0, len(cara1)):
    for j in range (0, 2):
        for k in range (0, len(cara1)):
            for l in range (0, 2):
                if cara1[i][j][0] == cara1[k][l][0] and cara1[i][j][1] == cara1[k][l][1] and i != k:
                    x.append(1)

if len(x) == len(cara1) * 2:
    print ("Ano")
else:
    print ("Ne")
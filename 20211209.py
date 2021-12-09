#【毎日Python】Pythonで配列の平均を算出する方法｜numpy.mean,nanmean
#https://www.youtube.com/watch?v=ikCqc1LGQxU

import numpy as np

a_1 = np.array([1,5,12,0,5,1])

np.mean(a_1) #平均を算出

a_2 = np.reshape(a_1,(2,3)) #２次元配列に
a_2

np.mean(a_2, axis=1) #行ごとの平均を算出

np.mean(a_2, axis=0) #列ごとの平均を算出
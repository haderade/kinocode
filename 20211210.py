#【毎日Python】Pythonで配列の単純平均・加重平均を取得する方法｜numpy.average
#https://www.youtube.com/watch?v=F-aM7yblyCs

import numpy as np

a = np.array([1,5,12,0,5,1])

np.average(a)

w = np.array([0.4,0.2,0.1,
              0.5,0.2,0.4])

np.average(a, weights=w)
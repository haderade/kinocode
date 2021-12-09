#【毎日Python】Pythonで欠損値のある配列の最大値・最小値を取得する方法｜numpy.nanmax,nanmin
#https://www.youtube.com/watch?v=kL3f40VThSk

import numpy as np

a = np.array([[1,2,3],
             [4,5,6],
             [7,8,np.nan]])

np.max(a)

np.min(a)

np.nanmax(a)

np.nanmin(a)

np.nanmax(a,axis=0) #行ごと

np.nanmin(a,axis=0) #行ごと

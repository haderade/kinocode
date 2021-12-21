#【毎日Python】Pythonで等間隔の配列を作成する方法｜numpy.linspace
#https://www.youtube.com/watch?v=SMiEcNi0ET8

import numpy as np

np.linspace(1,20) #等間隔の配列を作成。デフォルトの要素数は50
#array([ 1.        ,  1.3877551 ,  1.7755102 ,  2.16326531,  2.55102041,
#        2.93877551,  3.32653061,  3.71428571,  4.10204082,  4.48979592,
#        4.87755102,  5.26530612,  5.65306122,  6.04081633,  6.42857143,
#        6.81632653,  7.20408163,  7.59183673,  7.97959184,  8.36734694,
#        8.75510204,  9.14285714,  9.53061224,  9.91836735, 10.30612245,
#       10.69387755, 11.08163265, 11.46938776, 11.85714286, 12.24489796,
#       12.63265306, 13.02040816, 13.40816327, 13.79591837, 14.18367347,
#       14.57142857, 14.95918367, 15.34693878, 15.73469388, 16.12244898,
#       16.51020408, 16.89795918, 17.28571429, 17.67346939, 18.06122449,
#       18.44897959, 18.83673469, 19.2244898 , 19.6122449 , 20.        ])

np.linspace(1,20,10) #要素数を指定。ここでは10
#array([ 1.        ,  3.11111111,  5.22222222,  7.33333333,  9.44444444,
#       11.55555556, 13.66666667, 15.77777778, 17.88888889, 20.        ])

np.linspace(1,20,5,retstep=True) #上記に加えて差分を取得
#(array([ 1.  ,  5.75, 10.5 , 15.25, 20.  ]), 4.75)

np.linspace(1,20,5,endpoint=False) #最後の要素を含まずに配列を作成
#array([ 1. ,  4.8,  8.6, 12.4, 16.2])
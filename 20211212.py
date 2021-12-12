#【毎日Python】Pythonで配列の形状を変換する方法｜numpy.reshape
#https://www.youtube.com/watch?v=bNPbSbba23g&t=16s

import numpy as np

a = np.array([1,5,12,0,5,1]) #配列宣言

np.reshape(a,(2,3)) #二次元配列に変更、1値目：変更したい配列、２値目：タプルまたは形状を指定。タプルの中身は（行数,列数）
#array([[ 1,  5, 12],
#       [ 0,  5,  1]]


np.reshape(a,(3,1,2)) #三次元配列に変更、1値目：変更したい配列、２値目：タプルまたは形状を指定。タプルの中身は（次元数,行数,列数）
#array([[[ 1,  5]],
#
#       [[12,  0]],
#
#       [[ 5,  1]]])

np.reshape(a,(2,-1))
#array([[ 1,  5, 12],
#       [ 0,  5,  1]])
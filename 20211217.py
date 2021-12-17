#【毎日Python】Pythonで配列に末尾に要素を追加する方法｜numpy.append
#https://www.youtube.com/watch?v=1KeayphcL2k

import numpy as np

a_1 = np.array([1,2,3,4,5])

np.append(a_1,100) #末尾に値を追加
#array([  1,   2,   3,   4,   5, 100])

np.append(a_1,[50,55,60])#末尾に値をリストで追加
#array([ 1,  2,  3,  4,  5, 50, 55, 60])

a_2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

np.append(a_2,100) #一次元配列として値を追加
#array([  1,   2,   3,   4,   5,   6,   7,   8,   9, 100])

b = np.array([[10,20,30]])

np.append(a_2,b,axis=0) #行方向にbを追加(追加する列数は追加する列と同じにする)
#array([[ 1,  2,  3],
#       [ 4,  5,  6],
#       [ 7,  8,  9],
#       [10, 20, 30]])

c = np.array([[10],
              [20],
              [30]])

np.append(a_2,c,axis=1) #列方向にcを追加(追加する行数は追加する行と同じにする)
#array([[ 1,  2,  3, 10],
#       [ 4,  5,  6, 20],
#       [ 7,  8,  9, 30]])
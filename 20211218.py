#【毎日Python】Pythonで配列を横方向に結合する方法｜numpy.hstack
#https://www.youtube.com/watch?v=wR2Bys0viys

import numpy as np

a_1 = np.array([2,8,5])

a_2 = np.array([30,60,10])

np.hstack((a_1,a_2)) #a_1とa_2を横方向に結合
#array([ 2,  8,  5, 30, 60, 10])

a_1 = np.array([2,8,5])

a_4 = np.array([[40,20,70],
               [90,10,60,],
               [80,30,50]])

np.hstack((a_1,a_4)) #一次元配列と二次元配列を結合すると
#エラーが出る。行数が同じでないといけない

a_3 = np.array([[3,6,2,5,],
                [4,1,7,5],
                [3,5,8,5]])

a_4 = np.array([[40,20,70],
               [90,10,60,],
               [80,30,50]])

np.hstack((a_3,a_4)) #一次元配列と二次元配列を結合すると
#array([[ 3,  6,  2,  5, 40, 20, 70],
#       [ 4,  1,  7,  5, 90, 10, 60],
#       [ 3,  5,  8,  5, 80, 30, 50]])

a_1 = np.array([2,8,5])

a_2 = np.array([30,60,10])

np.vstack((a_1,a_2)) #vstack関数は縦方向に結合する
#array([[ 2,  8,  5],
#       [30, 60, 10]])


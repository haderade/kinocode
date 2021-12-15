#【毎日Python】Pythonで配列の値を条件を指定して置換する方法｜numpy.putmask
#https://www.youtube.com/watch?v=BGhqI7UtKJ4

import numpy as np

a_1 = np.array([1,5,2,6,8,3,4])

np.putmask(a_1,a_1 >= 5, 100) #5以上の値を100に変換
a_1 #array([  1, 100,   2, 100, 100,   3,   4])

a_2 = np.array([[1,7,5],
                [4,3,8],
                [12,2,1]])

np.putmask(a_2,a_2 >= 5, 100) #２次元配列でも5以上の値を100に変換
a_2
#array([[  1, 100, 100],
#       [  4,   3, 100],
#       [100,   2,   1]])

np.putmask(a_2,a_2 >= 5, [100,10]) #100or10に変換
a_2
#array([[  1,  10, 100],
#       [  4,   3,  10],
#       [100,   2,   1]])
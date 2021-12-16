#【毎日Python】Pythonで配列の軸を変換する方法｜numpy.transpose
#https://www.youtube.com/watch?v=OnkZv78HMGY&t=2255s

import numpy as np

a_1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

np.transpose(a_1) #配列の列と行を入れ替える。
#array([[1, 4, 7],
#       [2, 5, 8],
#       [3, 6, 9]])

a_2 = np.array([[[1,2,3,4]],
                [[5,6,7,8]],
                [[9,10,11,12]]])

np.transpose(a_2,(0,1,2)) #0が次元、1が行、2が列
#array([[[ 1,  2,  3,  4]],
#
#       [[ 5,  6,  7,  8]],
#
#       [[ 9, 10, 11, 12]]])

np.shape(a_2)
#(3, 1, 4)

np.transpose(a_2,(2,1,0))
#array([[[ 1,  5,  9]],
#
#       [[ 2,  6, 10]],
#
#       [[ 3,  7, 11]],
#
#       [[ 4,  8, 12]]])

np.transpose(a_2,(2,1,0)).shape
#(4, 1, 3)

np.transpose(a_2,(0,2,1))
#array([[[ 1],
#        [ 2],
#        [ 3],
#        [ 4]],
#
#       [[ 5],
#        [ 6],
#        [ 7],
#        [ 8]],
#
#       [[ 9],
#        [10],
#        [11],
#        [12]]])

np.transpose(a_2,(0,2,1)).shape
#(3, 4, 1)
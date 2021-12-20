#【毎日Python】Pythonで単位行列を作成する方法｜numpy.identity,eye
#youtube.com/watch?v=o5lP9lS3bVY

import numpy as np

np.identity(5) #単位行列を作成。引数に行列の数。
#array([[1., 0., 0., 0., 0.],
#       [0., 1., 0., 0., 0.],
#       [0., 0., 1., 0., 0.],
#       [0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 1.]])

np.eye(3,M=5,k=2) #行数と列数を指定して実行する場合はeye関数を使う。この場合、3が行数、M=5が列数、k=2が対角線の開始位置。
#array([[0., 0., 1., 0., 0.],
#       [0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 1.]])
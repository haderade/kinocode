#【毎日Python】Pythonで配列の値が条件に一致するかを判定する方法｜numpy.all
#https://www.youtube.com/watch?v=FyoMxl4i0z4

import numpy as np

a = np.array([[1,7,1,3,1],
              [0,1,0,3,1],
              [3,8,0,6,1]])

np.all(a) #0がある場合はFalse、0がない場合はTrue。この場合は全ての値が対象

np.all(a,axis=0) #axis=0は、列方向に判定

np.all(a,axis=1) #axis=1は、行方向に判定

np.all(a<5) #全ての値がa<5ならTrue

np.any(a<5) #参考(any関数)：いずれかの値がa<5ならTrue
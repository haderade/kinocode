# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LkLCiLLvQB7G80C-C1lGZeDygy9v219P
"""

import numpy as np

a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

a.max()

a.min()

a.max(axis=1) #列ごとの最大値

a.min(axis=1) #列ごとの最小値

a.max(axis=0) #行ごとの最大値

a.min(axis=0) #行ごとの最小値

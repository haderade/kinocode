# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uL5EtWmwFS5QFCymjV_EUy5JP5-bMPmO
"""

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
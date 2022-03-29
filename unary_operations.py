# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:24:50 2022

@author: DSP-LAB
"""

import numpy as np
arr=np.array([[1,5,6],[4,7,2],[3,1,9]])
print("largest element is:",arr.max())
print("row-wise maximum elements:",arr.max(axis=1))
print("column-wise minimum elements:",arr.min(axis=0))
print("sum of all array elements:",arr.sum())




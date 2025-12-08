import numpy as np
import time as t
import math
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    

try:
    nums_2d = np.genfromtxt('input.txt', dtype=int)
    ops = np.genfromtxt('ops.txt',dtype=str)
    nums_T=nums_2d.T
    ans = 0
    mask_add = (ops == '+')
    mask_mult = ~mask_add
    add_results = np.sum(nums_T[mask_add], axis=1)
    mult_results = np.prod(nums_T[mask_mult], axis=1)
    ans+= np.sum(add_results)+np.sum(mult_results)

    print(ans)
            
            
    
except ValueError:
    print("Val Error")


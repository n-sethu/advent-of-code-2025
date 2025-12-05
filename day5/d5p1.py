import numpy as np
import time as t
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')
pairs=[]
blank_index = lines.index('')
ranges = np.array([line.split('-') for line in lines[:blank_index]], dtype=int)
numbers = np.array([int(line) for line in lines[blank_index + 1:]])

n2d=numbers[:,np.newaxis]
starts= ranges[:,0]
ends = ranges[:,1]   
# print(ranges,numbers) 
in_range = (n2d>=starts) & (n2d<=ends)
ans = np.any(in_range,axis=1).sum()

print(ans)
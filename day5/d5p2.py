import numpy as np
import time as t
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')
pairs=[]
blank_index = lines.index('')
ranges = np.array([line.split('-') for line in lines[:blank_index]], dtype=int)

starts= ranges[:,0]
ends = ranges[:,1]   

ans = 0
sorted_indices = np.argsort(ranges[:, 0])  
sorted_ranges = ranges[sorted_indices]

curr_start = sorted_ranges[0][0]
curr_max = sorted_ranges[0][1]
for start,end in sorted_ranges:
    if start <= curr_max + 1:  
        curr_max = max(curr_max, end)  
    else:  # Gap found
        ans += (curr_max - curr_start + 1)  
        curr_start = start  
        curr_max = end

ans += (curr_max - curr_start + 1)
print(ans)

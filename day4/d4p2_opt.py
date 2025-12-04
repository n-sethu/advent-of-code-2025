import numpy as np
from scipy.ndimage import convolve
import time as t

with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

char_array = np.array([list(line) for line in lines])
tp_rolls = (char_array == '@').astype(int)

kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

total_removed = 0
start_time = t.perf_counter()
while True:
    neighbor_counts = convolve(tp_rolls, kernel, mode='constant', cval=0)
    
    accessible = (tp_rolls == 1) & (neighbor_counts < 4)
    
    num_removed = np.sum(accessible)
    
    if num_removed == 0:
        break
    
    tp_rolls[accessible] = 0
    total_removed += num_removed
end_time = t.perf_counter();
print(end_time-start_time)
# print(total_removed)
import numpy as np
import time as t
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

char_array = np.array([list(line) for line in lines])
tp_rolls = (char_array == '@').astype(int)

ROW_SIZE,COL_SIZE=tp_rolls.shape

def inBounds(i:int,j:int)->bool:
    return i<ROW_SIZE and i>=0 and j<COL_SIZE and j>=0

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

ans=0
def remove() -> int:
    local_ans=0
    for i in range(ROW_SIZE):
        for j in range(COL_SIZE):
            if tp_rolls[i][j]==1:
                curr_c=0
                for dx, dy in directions:
                        ni,nj = i+dx, j+dy
                        if inBounds(ni,nj) and tp_rolls[ni][nj]==1:
                            curr_c+=1                            
                if curr_c<4:
                    local_ans+=1
                    tp_rolls[i][j]=0
    return local_ans

start_time = t.perf_counter()
k = remove()
while k!=0:
    ans+=k
    k=remove()
    
end_time = t.perf_counter();
print(ans)
print(end_time-start_time)

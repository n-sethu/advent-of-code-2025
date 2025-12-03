import numpy as np
file = open("input.txt","r",newline ="")
ans =0
bank=np.zeros((200,100),dtype=int)
i=j=0

#parse
for line in file:
    for char in line.strip():
        bank[i][j]=int(char)
        j+=1
    i+=1
    j=0 

def getDig(arr, start,end)->list:
    toRet=[0,-1]
    
    for i in range(start,end):
        if(arr[i]>toRet[0]):
            toRet[0]=arr[i]
            toRet[1]=i
    return toRet

for row in bank:
    acc = ""
    pos = [-1, -1]
    for i in range(12):
        r= 12-i
        pos = getDig(row,pos[1]+1,len(row)-r+1)
        acc+=str(pos[0])
    ans += int(acc)

print(ans)
 
        
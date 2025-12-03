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
    
dig1=dig2=0
i=0
#solve
for row in bank:    
    for j in range(len(row)):
        if bank[i][j]>dig1 and j != len(row)-1:
            dig2=0
            dig1=bank[i][j]
        elif bank[i][j]>dig2:
            dig2=bank[i][j]
    ans+=int((str(dig1)+str(dig2)))
    i+=1
    dig1,dig2=0,0

        
print(ans)
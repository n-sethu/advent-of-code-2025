file = open("input.txt", "r")
curr =50
size=100
ans=0
for line in file:
    num = int(line[1:])
    if(line[0:1] == "L"):
        curr = (curr - num + size)%size
    else:
        curr = (curr+num)%size
    if curr==0:
        ans+=1
print(ans)
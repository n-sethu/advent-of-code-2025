file = open("input.txt","r",newline ="")
ans =0
def isRepeat(line:str)->bool:
    n = len(line)
    if n==1:
        return False
    for i in range(1,n//2 +1):
        if n%i!=0:
            continue
        mult = n//i
        if line == line[:i]*mult:
            return True
    return False

    


line = file.readline()
line_list = line.split(',')
for word in line_list:
    spl = word.split('-')
    start = int(spl[0].strip())
    end = int(spl[1].strip())
    for i in range(start,end+1):
        to_check = str(i)
        if isRepeat(to_check):
            ans+=i
print(ans)
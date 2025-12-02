file = open("input.txt","r",newline ="")
ans =0
def isRepeat(line:str)->bool:
    if len(line)%2 != 0:
        return False
    mid = len(line) // 2  
    return line[:mid] == line[mid:]
    

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
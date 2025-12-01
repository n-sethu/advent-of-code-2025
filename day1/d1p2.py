# bruteforce
SIZE = 100
START = 50


curr = START
cnt = 0
file = open("input.txt","r",newline ="")
for line in file:
    line = line.strip()
    if not line:
        continue
    dirc = line[0]
    x= int(line[1:])
    if dirc == 'R':
        for _ in range(x):
            curr = (curr + 1) % SIZE
            if curr == 0:
                cnt += 1
    else:
        for _ in range(x):
            curr = (curr - 1) % SIZE
            if curr == 0:
                cnt += 1
print(cnt)
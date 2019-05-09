temp, state = 0, True
start , end = 1, 10
cnt, find = 0, False

scope = 1000000

for i in range(10):
    cnt += 1
    if scope == cnt :
        temp = i
        find = True
        break

while not find :

    for i in range(start, end):
        cnt += 1
        if scope == cnt :
            temp = str(i)+str(i)[::-1]
            find = True
            break

    if find == False:
        for i in range(start,end):
            for j in range(0,10):
                cnt += 1
                if scope == cnt :
                    temp = str(i)+str(j)+str(i)[::-1]
                    find = True

    if start == 1 and end == 10 :
        start, end = 10, 100
    else :
        start, end = start * 10, end * 10

print(temp)
"""
arr = [a for a in range(1,11)]
del_arr = []
cnt = 0

while len(arr) != 1:
    for i in arr :
        cnt += 1
        if cnt == 3:
            print(del_arr)
            del_arr.append(i)
            cnt = 0

    for j in del_arr:
        print(j)
        arr.remove(j)
        del_arr = []
print(arr)
"""
"""
arr = [a for a in range(1,11)]
cnt = 0

def jose(arr, cnt):
    if len(arr) == 1:
        return arr
    elif len(arr) > 1 :
        for i in range(len(arr)) :
            if arr[i] != 0 :
                cnt += 1
            if cnt == 3 :
                arr[i] = 0
                cnt = 0
        jose(arr, cnt)


print(jose(arr, cnt))
"""
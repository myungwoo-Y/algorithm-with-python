test = "1D2S3T*"

arr = []

for i in range(len(test)):
    if test[i] == "S":
        arr.append(int(test[i-1]))
    elif test[i] == "D":
        arr.append(int(test[i-1]) **2)
    elif test[i] == "T":
        arr.append(int(test[i-1]) **3)
    elif test[i] == "#":
        arr[-1] = arr[-1] * (-1)
    elif test[i] == "*":
        if len(arr) > 1:
            for i in range(-2,0):
                arr[i] = arr[i] * 2
        else :
            arr[0] = arr[0] * 2

print sum(arr)


# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/


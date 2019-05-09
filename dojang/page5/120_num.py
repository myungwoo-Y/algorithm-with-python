def a(n):
    arr = [0 for a in range(n+1)]

    for i in range(1,n+1):
        cnt = i
        while cnt < n+1:
            arr[cnt] += 1
            cnt += i


    print(len([i for i, v in enumerate(arr) if v%2 != 0]))


a(120)
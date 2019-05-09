arr = list(range(1,21))

def a(arr):
    i,j = input("input num : ").split(" ")

    i = int(i)-1
    j = int(j)-1

    if j == -1 or i == -1 :
        return 0

    if (i-j) % 2 == 0 :
        num = (j-i) // 2
    else:
        num = (j-i) // 2 + 1

    for t in range(num):
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1 , j-1

    print(arr)

    a(arr)

a(arr)
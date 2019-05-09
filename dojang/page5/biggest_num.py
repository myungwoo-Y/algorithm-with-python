arr = input("input num : ").split(" ")

for i in range(1,len(arr)):
    for j in range(i):
        b = arr[i-j]
        a = arr[i-j-1]
        if int(b+a) > int(a+b):
            arr[i-j], arr[i-j-1] = arr[i-j-1], arr[i-j]
            print(b+a, a+b)

print("".join(arr))

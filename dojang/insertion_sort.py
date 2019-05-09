"""
def sort(arr):
    j, k, temp = 0, 0, 0

    for i in range(1,len(arr)):
        j, temp = 0, arr[i]

        while i > j :
            if arr[j] > arr[i]:
                k = j
                for n in range(0,i-k):
                    arr[i-n] = arr[i-n-1]
                arr[k] = temp
                break
            j += 1
    print arr

arr = [5,2,4,6,1,3]

sort(arr)
"""
def sort(arr):
    for i in range(1, len(arr)):
        for j in range( i ):
            while arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print arr

arr = [5,2,4,6,1,3]

sort(arr)
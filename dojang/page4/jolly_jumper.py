"""
a = 0
arr = input("input num : ").split(" ")

temp = [a for a in range(1,len(arr)-1)]

for i in range(1,len(arr)-1):
    a = (int(arr[i])-int(arr[i+1]))
    if a < 0 :
        a = a * -1
    print(a)
    if temp[a-1] != 0 and a <= len(temp):
        temp[a-1] = 0
    else :
        print("Not jolly")
        break
    if sum(temp) == 0 :
        print("Jolly")
"""

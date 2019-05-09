i, j = raw_input("input range : ").split()  # input value is splited by space

def prime(i, j):
    cnt = 0   # count is filled by 0 to defult
    prime_arr = []
    while i < j:   # if i is same with j,  this loop will be down
        cnt = 0
        for num in range(1,i):
            if i % num == 0:
                cnt += 1
        if cnt == 1 :
          prime_arr.append(i)
        i += 1
    return prime_arr

print prime(int(i), int(j))
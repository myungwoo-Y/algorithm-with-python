def three_plus(i, j):
    full_size = 0
    for num in range(i,j+1):
        size = 1
        while not num == 1:
            if num%2 == 0:
                num = num / 2
                size +=1
            else:
                num = num * 3 + 1
                size += 1
        if full_size < size :
            full_size = size
    return full_size

i, j = raw_input("iput number : ").split()

print three_plus(int(i), int(j))
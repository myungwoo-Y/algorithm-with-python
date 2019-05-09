row, col = input("input row and col : ").split(" ")

arr = [[0 for a in range(int(col))] for b in range(int(row))]

dx, dy=0, 1
cnt=1
x=y=0

while cnt <= int(row) * int(col):
    arr[x][y] = cnt
    x, y = x+dx, y+dy

    if (x >= int(row)) or(y >=int(col)) or arr[x][y] != 0:
        x, y = x-dx, y-dy
        if dx == 0 :
            dx,dy = dy,dx
        else:
            dx,dy = -dy,-dx
        x, y = x+dx, y+dy
    cnt += 1

for i in arr:
    print(i)


"""
def spiral_array(row, col):
    array = [[-1 for a in range(col)] for a in range(row)]
    i=j=n=0
    direction = 1
    temp_i=temp_j= 0

    while n < len(array) * len(array):
        if(i >= row) or(j >=col) or array[i][j] != -1:
            
            direction += 1
            if direction > 4:
                direction = 1

            i,j = convert(direction, temp_i, temp_j)
        else:
            array[i][j] = n
            temp_i = i
            temp_j = j
            i,j = convert(direction, i, j)
            n += 1

    for i in range(len(array)):
        print(array[i])


def convert(direction, i ,j):
    if direction == 1 :
        j += 1
    elif direction == 2:
        i += 1
    elif direction == 3:
        j += -1
    elif direction == 4:
        i += -1
    return i,j

spiral_array(6,6)
"""
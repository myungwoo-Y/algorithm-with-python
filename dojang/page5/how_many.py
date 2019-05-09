log = [[("09:12:23"),("11:14:35")],
       [("10:34:01"),("13:23:40")],
       [("10:34:31"),("11:20:10")],
       ]

cnt = 0

is_time = "11:05:20"

convert_time = int(is_time[0:2]) * 3600 + int(is_time[3:5]) * 60 + int(is_time[6:])    # time to integer

def convert(log):    # convert time array to integer array
    convert_log = [[0 for a in range(len(log[1]))] for b in range(len(log))]    # make array to same length of input log
    for i in range(len(log)):
        for j in range(len(log[1])):
            convert_log[i][j] = int(log[i][j][0:2]) * 3600 + int(log[i][j][3:5]) * 60 + int(log[i][j][6:])
    return convert_log

for arr in convert(log):
    if arr[0] < convert_time and arr[1] > convert_time:
        cnt += 1

print(cnt)


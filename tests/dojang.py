'''
all_arr = [x for x in range(1,5000)]
g_arr = []
cnt = 0
for i in range(1,5000):
    cnt = i   # already plus
    for y in str(i):  # y is string in i
        cnt += int(y)
    g_arr.append(cnt)
    cnt = 0   # default because next time is run well

for i in g_arr:
    if all_arr.count(i) > 0:
        all_arr.remove(i)

for i in g_arr:
    cnt += i

print cnt

'''
# this is bad case of my mind, Under is the best coding


'''
print sum(set(range(1,5000)) - {x + sum(int(a) for a in str(x)) for x in range(1,5000)})  # int(a) for a in str(x) 

'''



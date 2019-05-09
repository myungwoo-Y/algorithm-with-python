"""
def f(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i
    return sum

cnt = 0

for s in str(f(25))[::-1]:
    if s == "0":
        cnt += 1
    else:
        break

print(cnt)
"""

"""
def f(n):
    if n<5 : return 0
    return int(n/5) + f(n/5)

print(f(25))
"""

def f(x):
    cnt = 0
    for i in range(5, x+1):
        while i % 5 == 0 :
            cnt += 1
            i /= 5
    return cnt

print(f(25))

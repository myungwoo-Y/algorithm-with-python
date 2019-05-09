"""
s = "20000000"
n = 0
arr = []
for i in range(1,len(s)+1):
    arr.append(s[-1*i])
    n += 1
    if n == 3 :
        n = 0
        arr.append(",")


for j in range(1,len(arr)+1):
    print(arr[j * -1], end=" ")
"""

def comma(n):
    if n[0] == "-":
        return "-"+comma(n[1:])
    if len(n) <= 3:
        return n
    if n.find('.') == -1 :
        return comma(n[:-3]) + ',' + n[-3:]
    else:
        return comma(n[:n.find('.')]) + n[n.find('.'):]

print(comma('123456789.123'))



'''
test = 'aabcccaaaaas'
cnt = 1
a = ''
t = test + '@'
for text in t:
    if a != text and a != '':
        print a, cnt,
        cnt = 1
    elif a == text:
        cnt += 1
    a = text
'''
s = 'aabcccaaaaas'

result = s[0]
cnt = 0

for st in s:
    if st == result[-1]:
        cnt += 1
    else:
        result += str(cnt) + st
        cnt = 1
result += str(cnt)

print result






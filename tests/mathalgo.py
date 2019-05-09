'''
# Discrete find algorithm
a = [ x for x in range(1,2000) ]
x = 825
i = 1    # why i is 1 not 0 ? Because j is len(a) not len(a) -1
j = len(a)
while(j > i):
  m = (i+j) / 2
  if x > a[m]:
    i = m+1
  else:
    j = m

print a[m]
'''
'''
# bubble sort algorithm

a = [3, 5, 2, 1, 7]
temp = 0
for i in range(1,len(a)):
  for j in range(len(a)-i):
    if a[j] > a[j+1]:
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp

print a
'''

# insert sort algorithm

a = [3, 5, 2, 1, 7]





















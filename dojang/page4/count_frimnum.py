a, n= input().split()
a, n = int(a), int(n)

s = [0,0] + [1] * (n-1)

for i in range(2,int(n**.5)+1):
   if s[i]:
       s[i*2::i] = [0]*((n-i)//i)

for j in range(len(s)):
   if (j >= a and s[j]) :
      print(j)

"""
n = 600851475143
a = 2
b = 0
prime = True

while n > 0 :
    if n%a == 0 :
        print(a)

    a += 1
    n -=1
"""

def Largest_prime(n, cnt):
    while cnt < n:
        if n % cnt  ==  0:
            Largest_prime(n/cnt, cnt)
            return 0
        cnt += 1
    print(n)


Largest_prime(600851475143, 2)








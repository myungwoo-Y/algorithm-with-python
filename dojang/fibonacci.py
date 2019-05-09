"""
s = 0
d = 1
t = 1
temp = 0
limit = int(raw_input("input range : "))

while t+d < limit:

    temp = d
    t = d+t
    d = s+d
    s = temp

print s, d, t

"""

a, b = 0, 1
limit = int(input("input range : "))
print("0",)

while a < limit :
    a,b = b, a+b
    print(a,)

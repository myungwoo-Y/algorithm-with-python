test = ["a1", "a2", "a3", "b1", "b2", "b3"]

"""
def convert(test):
    result = [0 for a in range(len(test))]
    a = 0
    b = 1
    for s in test:
        if s[0] == "a":
            result[a] = s
            a += 2
        else :
            result[b] = s
            b += 2
    return result
"""

def convert(test):
    result = []
    for i,j in zip(test[:len(test)//2], test[len(test)//2:]):
        result.append(i)
        result.append(j)
    return result

print(convert(test))


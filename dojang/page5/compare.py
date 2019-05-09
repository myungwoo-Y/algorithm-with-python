def a(s1,s2):
    c = 0

    if len(s1) == len(s2):
        for i in range(len(s1)):
            t1 = s1[:i]+s1[i+1:]
            t2 = s2[:i]+s2[i+1:]
            if t1 == t2:
                return True

    elif len(s1) == len(s2)+1:
        if s1[:len(s1)-1] == s2 or s1[1:] == s2:
            return True


    elif len(s1)+1 == len(s2):
        if s1 == s2[:len(s2)-1] or s1 == s2[1:]:
            return True

    return False

s1, s2 = input("input str : ").split(" ")


print(a(s1,s2))
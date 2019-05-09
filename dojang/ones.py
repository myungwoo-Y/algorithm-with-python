test = 7
defult = 111
while True :
    if defult % test == 0:
        break
    else :
        defult = int(str(defult) +"1")

print len(str(defult))
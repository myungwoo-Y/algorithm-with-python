from random import randint


question = []

for i in range(0,4):
    while 1 :
        n = randint(0,9)
        if not question.count(n):
            question.append(n)
            break
count = 0

while 1 :
    ball = 0
    strike = 0
    answer = []
    for i in range(4):
        number = int(input("input number %d st: " %(i+1)))  # enter 1
        answer.append(number)
    print(answer)
    for i in range(4):
        if answer[i] == question[i]:
            strike += 1
        elif(question.count(answer[i]) == 1):
            ball += 1
    count += 1
    print ("#" * 20)
    print ("strike : {0} ,  ball : {1}" .format(strike, ball))
    print ("#" * 20 , count , "\n")
    if(answer == question or count == 8):
        print (question, "You win!")    # if array and string print ,  you have to use "," than "+"
        break


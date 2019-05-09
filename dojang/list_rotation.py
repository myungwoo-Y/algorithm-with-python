"""
exam = [-2, 1, 2, 3, 4]#raw_input("input string : ").split(" ")

def rotation(exam):
    test = exam[1:]
    result = []
    if exam[0] > 0:
        for i in range(((-1) * exam[0]), len(test)-exam[0]):
            result.append(test[i])
    else:
        for i in range(-1 * exam[0] - len(test),exam[0] * -1):
            result.append(test[i])
    print result

rotation(exam)
"""

exam = "312345"
amount = int(exam[0])
if int(exam[0]) > 0:
    result = exam[-1 * amount:] + exam[1:len(exam[1:])-amount]
else:
    result = exam[amount+1:] + exam[1:amount+1]

print(result)
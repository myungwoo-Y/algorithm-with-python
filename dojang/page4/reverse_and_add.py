"""
def reverse(n):
    cnt = 0
    while not str(n) == str(n)[::-1] or n < 10 :
        n = int(int(str(n))+int(str(n)[::-1]))
        print(n)
        cnt += 1

    return n, cnt

print(reverse(265))
"""

import math


def check_palindrome(str):
    for i in range(math.floor(len(str) / 2)):
        if str[i] != str[-i + -1]:
            return False
    return True


def reverse_and_add(n, in_num_str):
    try:
        if n < 1000:
            if check_palindrome(in_num_str):
                return print("%d %s" % (n, in_num_str))
            else:
                reverse_and_add(n + 1, str(int(in_num_str) + int(in_num_str[::-1])))
    except RecursionError:
        print("No palindrome within 1000 cycle")


how_many = int(input("How many numbers? "))
in_numbers = []

for i in range(how_many):
    in_numbers.append(input("Enter number: "))

for j in in_numbers:
    reverse_and_add(0, j)


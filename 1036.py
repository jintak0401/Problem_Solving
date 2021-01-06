from sys import stdin
from collections import deque

def digit_converter(num):
    
    ret_val = deque([])
    while num != 0:
        char = num % 36
        if char < 10:
            char = str(char)
        else:
            char = chr(ord('A') + (char - 10))
        ret_val.appendleft(char)
        num //= 36

    return ret_val

input = stdin.readline

input_num = int(input())

dic = {}

ans = 0

for _ in range(input_num):
    
    num = input().rstrip()

    for i in range(len(num)):

        digit = 36 ** i

        if num[-i - 1] in dic:
            dic[num[-i - 1]] += digit
        else:
            dic[num[-i - 1]] = digit

        if num[-i - 1].isnumeric():
            ans += int(num[-i - 1]) * digit

        else:
            ans += digit * (ord(num[-i - 1]) - ord('A') + 10)


dic = list(dic.items())
dic.sort(reverse=True, key = lambda x : (x[1] * (35 - int(x[0]) if x[0].isnumeric() else ord('Z') - ord(x[0]))))

k = int(input())

for i in range(k):

    if dic[i][0].isnumeric():
        ans += dic[i][1] * (35 - int(dic[i][0]))

    else:
        ans += dic[i][1] * (ord('Z') - ord(dic[i][0]))

    if i == len(dic) - 1:
        break


ans = digit_converter(ans)
print(''.join(ans) if len(ans) > 0 else 0)

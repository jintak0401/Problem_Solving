import math

retval = []

def operating(num, oper, value, index):

    global retval  
    
    if index == len(num):
        retval.append(value)
        return
    else:
        if oper[0] != 0:
            oper[0] -= 1
            operating(num, oper, value + num[index], index + 1)
            oper[0] += 1
        if oper[1] != 0:
            oper[1] -= 1
            operating(num, oper, value - num[index], index + 1)
            oper[1] += 1
        if oper[2] != 0:
            oper[2] -= 1
            operating(num, oper, value * num[index], index + 1)
            oper[2] += 1
        if oper[3] != 0:
            oper[3] -= 1
            if value < 0:
                value = -((-value) // num[index])
            else:
                value //= num[index]
            operating(num, oper, value, index + 1)
            oper[3] += 1


unit = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_val = - (10 ** 10)
min_val = - max_val

operating(num, oper, num[0], 1)

for i in retval:
    if max_val < i:
        max_val = i
    if min_val > i:
        min_val = i

print(max_val)
print(min_val)




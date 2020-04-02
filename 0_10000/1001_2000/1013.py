from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 5)

def check(num):

    if len(num) == 0:
        return True

    elif num[0] == '1':
        if len(num) < 4:
            return False
        elif num[1] == '0' and num[2] == '0':
            offset = 3
            while offset < len(num) and num[offset] == '0':
                offset += 1
            if offset == len(num):
                return False
            else:
                while offset < len(num) and num[offset] == '1':
                    offset += 1
                if offset == len(num):
                    return True
                else:
                    if check(num[offset:]) or (num[offset - 2] == '1' and check(num[offset - 1:])):
                        return True
                    else:
                        return False
    else:
        if len(num) <= 1:
            return False
        elif num[1] == '1':
            if check(num[2:]):
                return True
            else:
                return False

    return False


def solve(num):

    if check(num):
        return 'YES'
            
    else:
        return 'NO'


input = stdin.readline
case = int(input())

for _ in range(case):
    print(solve(input().rstrip())) 

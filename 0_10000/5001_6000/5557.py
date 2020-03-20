import sys

ans = 0

def calculate(num, index, val, cache):
    global ans 

    if index != len(num) - 1:
        if cache[val][index] == -1:
            cache_val = 0
            tmp_val = val + num[index]
            if 0 <= tmp_val <= 20:
                cache_val += calculate(num, index + 1, tmp_val, cache)
            tmp_val = val - num[index]
            if 0 <= tmp_val <= 20:
                cache_val += calculate(num, index + 1, tmp_val, cache)
            cache[val][index] = cache_val
            return cache_val
        else:
            return cache[val][index]
    
    else:
        if val == num[-1]:
            return 1
        else:
            return 0


            
length = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

cache = [[-1 for j in range(len(num))] for i in range(21)]

ans = calculate(num, 1, num[0], cache)

print(ans)


from sys import stdin

input = stdin.readline

target = int(input())

broken = []

if int(input()) != 0:
    broken = set(input().rstrip().split())

available = set([str(i) for i in range(10)]) - set(broken)

if len(broken) == 10:
    print(abs(target - 100))

else:
    
    up = target
    down = target

    upper_bound = max(2 * target, 100)
    lower_bound = 0

    ans = 0
    seq = 1
    num = 0

    while True:

        # down
        if seq:
            if down >= lower_bound:
                tmp = set(list(str(down)))
                if tmp & available == tmp or down == 100:
                    num = down
                    break
                else:
                    down -= 1

        # up
        else:
            if up <= upper_bound:
                tmp = set(list(str(up)))
                if tmp & available == tmp or up == 100:
                    num = up
                    break
                else:
                    up += 1
                    ans += 1
                    

        seq ^= 1

    print(min(ans + min(abs(num - 100), len(str(num))), abs(target - 100)))

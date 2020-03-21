
from sys import stdin

input = stdin.readline
minute = int(input())

ans = 0

s = []

time = 0
score = 0


for _ in range(minute):

    user_input = list(map(int, input().split()))

    if user_input[0] == 0:

        time -= 1

    else:
        s.append((time, score))
        time = user_input[2] - 1
        score = user_input[1]

    if time == 0:
        ans += score
        time, score = s.pop()


print(ans)

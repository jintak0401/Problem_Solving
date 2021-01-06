from sys import stdin


input = stdin.readline


day, kind = map(int, input().split())

desert = []

for _ in range(kind):
    desert.append(list(map(int, input().split())))


dp = [[desert[i][0], 0] for i in range(kind)] 

idx = 0

for i in range(1, day):
    
    for j in range(kind):

        for k in range(kind):
            val = dp[k][idx] + (desert[j][i] if j != k else desert[j][i] // 2)
            # print('%d + %d = %d'%(dp[k][idx], (desert[j][i] if j != k else desert[j][i] // 2), val))
            if val > dp[j][idx ^ 1]:
                dp[j][idx ^ 1] = val

    idx ^= 1


ans = -1
for i in range(kind):
    if ans < dp[i][idx]:
        ans = dp[i][idx]

print(ans)

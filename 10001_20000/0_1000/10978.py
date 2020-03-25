
ans = [0 for i in range(21)]

ans[1] = 0
ans[2] = 1
ans[3] = 2

for i in range(4, 21):
    ans[i] = (i - 1) * (ans[i - 1] + ans[i - 2])

case_num = int(input())

for _ in range(case_num):
    print(ans[int(input())])

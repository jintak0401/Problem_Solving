from sys import stdin
input = stdin.readline

work_num = int(input())
work = [0] * (work_num + 1)
for i in range(1, work_num + 1):

    _work = list(map(int, input().split()))
    cost = _work[0]
    edge = _work[2:]

    for tmp in edge:
        work[i] = max(work[tmp], work[i])
    work[i] += cost

print(max(work))

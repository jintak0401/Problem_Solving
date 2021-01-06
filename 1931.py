from sys import stdin

num_case = int(stdin.readline())

time = []

for i in range(num_case):
    s, e = map(int, stdin.readline().split())
    time.append([s, e])

time = sorted(time, key = lambda x : (x[1], x[0]))

before = time[0]
ans = 1
index = 1
while index < (len(time)):
    after = time[index]
    if (before[1]) <= after[0]:
        before = after
        ans += 1
    index += 1


print(ans)


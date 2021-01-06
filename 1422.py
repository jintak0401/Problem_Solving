def sorting(num):

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            a = int(num[i] + num[j])
            b = int(num[j] + num[i])
            if a < b:
                num[i], num[j] = num[j], num[i]


k, n = map(int, input().split())

num = []

for i in range(k):
    num.append(input())

max_val = max(list(map(int, num)))
sorting(num)

check = True

ans = ''

for i in range(k):
    ans += num[i]
    if check and num[i] == str(max_val):
        ans += num[i] * (n - k)
        check = False

print(ans)


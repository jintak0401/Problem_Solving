
n, r = map(int, input().split())

arr = [1 for _ in range(n + 1)]

for i in range(1, len(arr) // 2 + (len(arr) % 2)):
    arr[i] = arr[i - 1] * (len(arr) - i) // i

for i in range(1, len(arr) // 2):
    arr[-i - 1] = arr[i]


print(arr[r] % 10007)

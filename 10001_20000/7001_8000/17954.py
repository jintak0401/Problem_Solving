num = int(input())

if num == 1:
    print(2)
    print('1\n2')
    exit()

arr = [[0 for _ in range(num)] for _ in range(2)]
arr[0][0], arr[0][-1], arr[1][-1], arr[1][0] = 2 * num, 2 * num - 1, 2 * num - 2, 2 * num - 3

for i in range(1, num - 1):
    arr[0][i] = i
    arr[1][-1 - i] = i + num - 2

rotten = 0
time = 1
t = 2
for i in range(1, num):
    rotten += time * arr[1][i]
    time += t
    t += 1

for i in range(len(arr[0]) - 1, -1, -1):
    rotten += time * arr[0][i]
    time += t
    t += 1

# print(((2 * num - 1) * (2 * num + 13) * num + 3) * num // 6)
print(*arr[0])
print(*arr[1])


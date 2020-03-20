from sys import stdin

input = stdin.readline

length = int(input())

arr = []

for _ in range(length):
    arr.append(list(map(int, input().split())))
    

tmp = [i for i in arr[length - 1]]

max_arr = []

for i in range(len(arr) - 1, 0, -1):

    max_arr = [arr[i - 1][j] + max(tmp[j], tmp[j + 1]) for j in range(len(arr[i - 1]))]

    tmp = max_arr


print(max_arr[0])


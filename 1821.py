from sys import stdin
input = stdin.readline

arr = []
comb = []
F = 0

def right_rotate(start, end):
    global arr
    last = arr[end]

    for i in range(end, start, -1):
        arr[i] = arr[i-1]
    arr[start] = last

def left_rotate(start, end):
    global arr
    first = arr[start]

    for i in range(start, end):
        arr[i] = arr[i + 1]
    arr[end] = first

def perm(depth):

    global arr, comb, F

    if depth == len(arr) - 1:
        val = sum([a * b for a, b in zip(arr, comb)])
        if val == F:
            return True

    else:
        for i in range(depth, len(arr)):
            right_rotate(depth, i)
            if (perm(depth + 1)):
                return True
            left_rotate(depth, i)

def solve():

    global arr, comb, F
    N, F = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    comb = [0 for i in range(N)]
    comb[0] = 1
    comb[-1] = 1

    for i in range(1, (N // 2) + (N % 2)):
        comb[i] = comb[i-1] * (N - i) // i
        comb[-i-1] = comb[i]

    perm(0)

    print(*arr)

solve()

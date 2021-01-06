from sys import stdin

def exchange_all(arr, start, mid, end):
    front_val = arr[start]
    behind_val = arr[mid]

    for i in range(start, start + (end - mid)):
        arr[i] = behind_val
    for i in range(start + (end - mid), end):
        arr[i] = front_val

input = stdin.readline
input()

arr = list(map(int, input().split()))

arr = sorted(arr)

i = 1

while i < len(arr):
    
    if arr[i] == arr[i - 1] + 1:
        mid = i
        start = i - 1
        end = i + 1
        while start >= 0 and arr[start] == arr[mid] - 1:
            start -= 1
        start += 1
        while end < len(arr) and arr[end] == arr[mid]:
            end += 1

        if end == len(arr):
            exchange_all(arr, start, mid, end)
            i = end

        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            i = end + 1

    else:
        i += 1


print(' '.join(map(str, arr)))

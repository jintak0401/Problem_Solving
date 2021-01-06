from collections import deque

length = int(input())

arr = [0 for i in range(3)]
arr = deque(arr)
arr[1], arr[2] = 1, 1

if length >= 3:
    length %= 15 * (100000)
    arr.popleft()
    index = 2
    while index != length:
        arr.append(sum(arr))
        arr.popleft()

        if arr[-1] >= 1000000:
            arr[-1] %= 1000000
        
        index += 1

    # print(arr)
    print(arr[-1])

else:
    print(arr[length])

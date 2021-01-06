
def fibo(arr, seq):
    if seq == 0:
        return 0

    elif arr[seq] != 0:
        return arr[seq]

    else:
        ret_val = fibo(arr, seq -1) + fibo(arr, seq - 2)
        arr[seq] = ret_val
        return ret_val



length = int(input())
arr = [0 for i in range(max(length + 1, 3))]
arr[1], arr[2] = 1, 1

print(fibo(arr, length))

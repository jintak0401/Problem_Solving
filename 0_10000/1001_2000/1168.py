n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]

idx = -1
ans = []
while arr:
   
    idx = (idx + k) % len(arr)
    ans.append(arr[idx])
    arr.pop(idx)
    idx -= 1

ans = '<' + ', '.join(map(str, ans)) + '>'

print(ans)



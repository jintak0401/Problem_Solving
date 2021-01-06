from collections import deque

n, k = map(int, input().split())

q = deque([])
visited = set([])

q.append(n)
ans = 0

while True:

    q_size = len(q)

    for i in range(q_size):
        pos = q.popleft()
        if pos == k:
            print(ans)
            exit(0)

        if pos - 1 not in visited:
            q.append(pos - 1)
            visited.add(pos - 1)

        if pos < k:
            if pos + 1 not in visited:
                q.append(pos + 1)
                visited.add(pos + 1)
            if 2 * pos not in visited:
                q.append(2 * pos)
                visited.add(2 * pos)

    ans += 1



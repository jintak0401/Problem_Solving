n, l = map(int, input().split())


def get_ans():

    start = -1
    length = l

    while length <= 100:

        if length % 2 == 1 and (n // length) * length  == n:
            return n // length - (length - 1) // 2, length
        elif length % 2 == 0 and (n // (length // 2)) * (length // 2) == n and (n // (length // 2)) % 2 == 1:
            return (n // (length // 2)) // 2 - (length // 2 - 1), length
        length += 1
    
    return -1, -1
            


start, length = get_ans()
if start < 0:
    print(-1)
else:
    for i in range(start, start + length):
        print(i, end = ' ')


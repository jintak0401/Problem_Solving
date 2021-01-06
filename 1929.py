def get_prime(start, end):

    prime = []

    if start == 1:
        start += 1

    if start % 2 == 0 and start <= end:
        if start == 2:
            prime.append(2)
        start += 1

    for i in range(start, end + 1, 2):
        check = True
        for j in range(3, int((i ** 0.5) + 1), 2):
            if i % j == 0:
                check = False
                break
        if check:
            prime.append(i)
    
    return prime

    




start, end = map(int, input().split())

prime = get_prime(start, end)

for i in prime:
    print(i)


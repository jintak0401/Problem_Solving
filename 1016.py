import math

# def rough_ans(start, end):

    # prime = list(range(start, end + 1))

    # for i in range(2, int(end ** 0.5) + 1):
        # i **= 2
        # j = 1
        # while i * j <= end:
            # if prime.count(i * j) > 0:
                # prime.remove(i * j)
            # j += 1

    # print('< rough >')
    # print(prime)
    # print('\nnum :', len(prime))

def get_prime(x):
    start, end = 3, int(x ** 0.5)

    prime = [2]

    for i in range(3, end + 1, 2):
        check = True
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                check = False
                break
        if check:
            prime.append(i)
    return prime

def get_ans(start, end):
    prime = get_prime(end)

    num = []

    # ans = list(range(start, end + 1))
    for i in prime:
        i **= 2
        for j in range(math.ceil(start / i), math.floor(end / i) + 1):
            if (i * j <= end):
                num.append(i * j)
    num = list(set(num))

    return end - start + 1 - len(num)

start, end = map(int, input().split())


# rough_ans(start, end)
# print('\n===================================\n')
# print('< own >')
# print('num :', get_ans(start, end))

print(get_ans(start, end))


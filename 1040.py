n, k = map(int, input().split())

n = list(str(n))

if len(set(n)) == k:
    print(''.join(n))

else:

    for i in range(len(n) - 1, -1, -1):
        for j in range(int(n[i]) + 1, 10):

            num = n[:i] + [str(j)]
            left_kind = k - len(set(num))
            left_num = set([str(i) for i in range(10)]) - set(num)
            len_left = len(n) - (i + 1)

            if left_kind < 0 or len(left_num) < left_kind or len_left < left_kind:
                continue

            left_num = sorted(list(left_num))

            if left_kind == 0:
                print(''.join(num + [min(num)] * len_left))

            else:
                print(''.join(num + ['0'] * (len_left - left_kind) + left_num[:left_kind]))
            
            exit()


    n = max(k, len(n) + 1)
    print('1' + '0' * (n - k + 1) + "23456789"[:k - 2])

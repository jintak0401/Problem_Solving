from sys import stdin
from collections import defaultdict
input = stdin.readline

def solve(know, party, people):
    additional = set()

    for person in know:
        for _party in people[person]:
            additional |= party[_party]
    additional -= know

    while len(additional) > 0:
        know |= additional
        tmp = set()
        for person in additional:
            for _party in people[person]:
                tmp |= party[_party]
        additional = tmp
        additional -= know

    ret_val = 0
    for val in party.values():
        if len(know & val) == 0:
            ret_val += 1

    return ret_val

n, m = map(int, input().split())

know = list(map(int, input().split()))
know = set(know[1:])
party = defaultdict(set)
people = defaultdict(set)
for i in range(m):
    tmp = list(map(int, input().split()))
    party[i] |= set(tmp[1:])
    for j in party[i]:
        people[j] |= {i}
print(solve(know, party, people))

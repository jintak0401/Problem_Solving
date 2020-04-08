from sys import stdin
input = stdin.readline

def solve(string, compare):

    r_compare = compare[::-1]
    left_str, right_str = [], []
    left, right = 0, len(string) - 1
    left_turn = True 
    while left <= right:
        if left_turn:
            left_str.append(string[left])
            left += 1
            if left_str[-len(compare):] == compare:
                left_str[-len(compare):] = []
                left_turn = False
        else:
            right_str.append(string[right])
            right -= 1
            if right_str[-len(compare):] == r_compare:
                right_str[-len(compare):] = []
                left_turn = True
   
    ans = []
    if len(left_str) > 0:
        ans += left_str
    if len(right_str) > 0:
        ans += right_str[::-1]

    ans = ''.join(ans)
    compare = ''.join(compare)
    idx = ans.find(compare)
    while idx != -1:
        ans = ans[:idx] + ans[idx + len(compare):]
        idx = ans.find(compare)
    
    return ans

compare = list(input().rstrip())
string = input().rstrip()
print(solve(string, compare))

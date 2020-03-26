from sys import stdin
from collections import deque
from itertools import combinations
from copy import deepcopy

input = stdin.readline
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 0 --> 호수 / 1 --> 그냥 땅 / 2 --> 배양액 땅 / 3 --> green / 4 --> red / 5 --> flower

field = []
growing_pt = set()   # 배양액을 뿌릴 땅

row, col, green, red = map(int, input().split())

for i in range(row):
    tmp_row = list(map(int, input().split()))
    field.append(tmp_row)
    for j in range(len(tmp_row)):
        if tmp_row[j] == 2:
            growing_pt.add((i, j))

green_pt = list(combinations(growing_pt, green))  # 초록 배양액을 뿌릴 땅을 combinations 을 통해 얻어냄

ans = 0

for i in range(len(green_pt)):

    red_pt = growing_pt - set(green_pt[i])
    red_pt = list(combinations(red_pt, red))   # 빨간 배양액을 뿌릴 땅을 combinations 을 통해 얻어냄

    for j in range(len(red_pt)):
    
        tmp_ans = 0
        dic = {}   # 모든 경우마다 배양액을 뿌리고 퍼진 자리, 꽃이 핀 자리를 dictionary 로 관리
        green_q = deque([])  # 초록 배양액의 bfs 를 위한 deque
        red_q = deque([])    # 빨간 배양액의 bfs 를 위한 deque
        for point in green_pt[i]:
            green_q.append(point)  # 맨 처음 초록 배양액을 뿌릴 자리
            dic[point] = [3, 0]
        for point in red_pt[j]:
            red_q.append(point)    # 맨 처음 빨간 배양액을 뿌릴 자리
            dic[point] = [4, 0]
        
        step = 1

        while red_q and green_q:  # 빨간/초록 배양액 모두 퍼질 수 있을 때까지 

            q_size = len(green_q)

            for _ in range(q_size):   # 초록 배양액 bfs

                point = green_q.popleft()

                if point in dic and dic[point][0] == 5:   # 전 단계에서 개화했을 경우, 해당 자리에서 주변으로 전파가 안되므로 continue
                    continue

                for dx, dy in d:
                    x, y = point[0] + dx, point[1] + dy

                    if 0 <= x < row and 0 <= y < col and (x, y) not in dic:   # (x, y) 가 dic 에 있다면, 해당 자리에 어떤색 배양액이든 전파가 불가능하므로 not in
                        if (field[x][y] == 1 or field[x][y] == 2):  # 원래 field 에서 1, 2 인 땅에만 전파가 가능하므로
                            dic[(x, y)] = [3, step]  # 3 은 초록 배양액(9번줄 참고), step 은 빨간 배양이 동시에 전파된 것인지 판단하기 위한 값
                            green_q.append((x, y))


            q_size = len(red_q)

            for _ in range(q_size): # 빨간 배양액 bfs

                point = red_q.popleft()
                for dx, dy in d:
                    x, y = point[0] + dx, point[1] + dy

                    if 0 <= x < row and 0 <= y < col:
                        if (x, y) in dic and dic[(x, y)] == [3, step]: # 이번 단계에서 해당 자리에 초록 배양액이 전파된 경우
                            dic[(x, y)][0] = 5
                            tmp_ans += 1

                        elif (x, y) not in dic and (field[x][y] == 1 or field[x][y] == 2): # 어떠한 배양액도 전파되지 않은 땅이 field 에서 1, 2 일 경우
                            dic[(x, y)] = [4, step] # 4 는 빨간 배양액(9번줄 참고)
                            red_q.append((x, y))

            step += 1

        ans = max(ans, tmp_ans) # 모든 경우마다 가능한 꽃의 개수 중 최대값을 ans 로 저장

print(ans)

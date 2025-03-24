import sys
sys.stdin = open('input.txt', 'r')

def pick(cnt, i):
    if cnt == N//2:
        food1 = []
        food2 = []
        for n in range(N):
            if visited[n] == 1:
                food1.append(n)
            else:
                food2.append(n)
        # print(food1, food2)
        food1_sum = 0
        food2_sum = 0
        for ci in range(cnt):
            for cj in range(ci+1, cnt):
                food1_sum += (foods[food1[ci]][food1[cj]] + foods[food1[cj]][food1[ci]])
                food2_sum += (foods[food2[ci]][food2[cj]] + foods[food2[cj]][food2[ci]])
        return abs(food1_sum - food2_sum)
    
    if i == N-1:
        return 
    
    visited[i] = 1
    pick(cnt+1, i+1)
    visited[i] = 0
    pick(cnt+1, i+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    foods = [[*map(int, input().split())] for _ in range(N)]
    visited = [0]*N
    result = 160000
    result = min(result, pick(0, 0))
    print(result)
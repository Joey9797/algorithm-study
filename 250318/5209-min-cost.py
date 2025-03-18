import sys
sys.stdin = open('input.txt', 'r')

def pick_factory(cnt, cost):
    global min_cost, visited

    if cost >= min_cost:
        return

    if cnt == N:
        min_cost = min(cost, min_cost)
        return
    
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            pick_factory(cnt+1, cost + cost_lst[cnt][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_cost = 22275
    cost_lst = [[*map(int, input().split())] for _ in range(N)]
    visited = [0]*N
    pick_factory(0, 0)
    print(f"#{tc} {min_cost}")
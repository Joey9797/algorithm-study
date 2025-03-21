import sys
sys.stdin = open("input.txt", "r")
import heapq
'''
PRIM 으로 품----------------------------------------------------------------
'''
# 1. 시작 정점 정해서, 간선 전부 큐에 저장
# 2. 힙큐 사용해서 가장 짧은 간선 선택
# 3. 정점 visited 처리
def prim(s):
    hq = [(0, s)]
    total = 0
    while hq:
        w, node = heapq.heappop(hq)

        if visited[node]:
            continue

        visited[node] = 1
        total += w
        for nw, n_node in graph[node]:
            heapq.heappush(hq, (nw, n_node))
    return round(total*E)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    graph = [[] for _ in range(N)]
    visited = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            graph[i].append(((x[i]-x[j])**2 + (y[i]-y[j])**2, j))
            graph[j].append(((x[i]-x[j])**2 + (y[i]-y[j])**2, i))
    print(f"#{tc} {prim(0)}")
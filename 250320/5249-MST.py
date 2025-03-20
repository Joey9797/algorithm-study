import sys
sys.stdin = open("input.txt", "r")
import heapq

def prim(node):
    q = [(0, node)]
    visited = [0] * (V+1)
    min_w = 0

    while q:
        # 가중치가 작은 것부터 튀어나온다
        w, node = heapq.heappop(q)

        if visited[node]:
            continue

        visited[node] = 1
        min_w += w

        for w, next_node in graph[node]:
            if visited[next_node]:
                continue
            heapq.heappush(q, (w, next_node))
            
    return min_w
    

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w, s))
    # print(graph)
    print(f"#{tc} {prim(0)}")
    

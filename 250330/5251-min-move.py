import sys
sys.stdin = open('input.txt', 'r')
import heapq

def dijkstra(S):
    heapq.heappush(hq, (0, S))
    dist[S] = 0
    while hq:
        w, s = heapq.heappop(hq)
        for ew, e in graph[s]:
            nw = w + ew
            if nw < dist[e]:
                dist[e] = nw
                heapq.heappush(hq, (nw, e))


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    INF = float('inf')
    dist = [INF] * (N+1)
    hq = []
    dijkstra(0)
    print(f"#{tc} {dist[N]}")
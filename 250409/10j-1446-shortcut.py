import sys
input = sys.stdin.readline

N, D = map(int, input().split()) # 지름길 개수 N, 목적지 D
graph = [[] for _ in range(D+1)]    # 모든 정점 등록 (0번부터 D번까지)
for _ in range(N):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
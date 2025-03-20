import sys
sys.stdin = open("input.txt", "r")
'''
KRUSKAL로 품. 좀 느림----------------------------------------------------------------
'''
def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x_king = find(x)
    y_king = find(y)

    if x_king != y_king:
        parents[y_king] = x_king

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 섬 개수 N
    x_info = [*map(int, input().split())]
    y_info = [*map(int, input().split())]
    graph = []
    parents = list(range(N))
    for i in range(N):
        for j in range(i+1, N):
            w = (x_info[i] - x_info[j])**2 + (y_info[i] - y_info[j])**2
            graph.append((w, i, j))
    graph.sort(key=lambda x: x[0])
    
    cnt = 0
    min_w = 0
    for w, i, j in graph:
        if find(i) != find(j):
            union(i, j)
            cnt += 1
            min_w += w
            if cnt == N-1:
                break
    E = float(input())
    print(f"#{tc} {round(min_w*E)}")
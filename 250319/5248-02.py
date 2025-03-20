import sys
sys.stdin = open("input.txt", "r")
'''
서로소 집합으로 풀기 ----------------------------------------------------------------
'''
def find_set(x):
    if graph[x] == x:
        return x

    graph[x] = find_set(graph[x])
    return graph[x]

def union(x, y):
    x_root = find_set(x)
    y_root = find_set(y)

    if x_root != y_root:
        graph[y_root] = x_root


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [*map(int, input().split())]
    graph = list(range(N+1))
    for i in range(0, M*2, 2):
        p, c = info[i], info[i+1]
        union(p, c)

    kings = set()
    for i in range(1, N+1):
        kings.add(find_set(i))
    print(graph)
    print(f"#{tc} {len(kings)}")
    
import sys
sys.stdin = open("input.txt", "r")

def find_set(x):
    if graph[x] == x:
        kings.add(x)
        return 

    find_set(graph[x])
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [*map(int, input().split())]
    graph = list(range(N+1))
    for i in range(0, M*2, 2):
        p, c = info[i], info[i+1]
        if p < c:
            graph[c] = p
        else:
            graph[p] = c
    kings = set()
    for i in range(1, N+1):
        find_set(i)
    print(f"#{tc} {len(kings)}")
    
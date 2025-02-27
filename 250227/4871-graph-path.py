'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''
def find_path(s, e, info):
    stack = [s]
    visited = [0] * (V+1)
    visited[s] = 1
    v = s
    while stack:
        if v == e:
            return 1
        for t in info[v]:
            if visited[t] == 0:
                stack.append(t)
                visited[t] = 1
                v = t
                break
        else:
            v = stack.pop()
            if info[v] == False:
                return 0
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    info = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = list(map(int, input().split()))
        info[a].append(b)
    s, e = list(map(int, input().split()))
    result = find_path(s, e, info)
    print(f'#{tc} {result}')
    
'''
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7'''
def find_way(s, e, info):
    stack = [s]
    visited = [0]*100
    visited[s] = 1
    v = s
    while stack:
        if v == e:
            return 1
        else:
            for t in info[v]:
                if visited[t] == 0:
                    stack.append(t)
                    visited[t] = 1
                    v = t
                    break
            else:
                v = stack.pop()
    return 0

for _ in range(10):
    T, K = list(map(int, input().split()))
    info = [[] for _ in range(100)]
    s, e = 0, 99
    graph = list(map(int, input().split()))
    for i in range(0, 2*K, 2):
        v1, v2 = graph[i], graph[i+1]
        info[v1].append(v2)
    result = find_way(s, e, info)
    print(f'#{T} {result}')
    

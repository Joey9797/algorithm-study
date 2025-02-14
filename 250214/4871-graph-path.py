T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split())) # V:노드 개수 E:경로 개수
    graph = [list(map(int, input().split())) for _ in range(E)]
    adj_lst = [[] for _ in range(V+1)]
    for g in graph:
        s, e = g[0], g[1]
        adj_lst[s].append(e)
    for a in adj_lst:
        if not a: # a == [] 랑 같은 뜻
            a.append(0)
    S, G = list(map(int, input().split())) # S:시작점 G:도착점
    print(adj_lst)
    def dfs(S, G):   # S = 시작지점 , G = 도착지점
        stack = []
        visited = [0] * (V + 1)
        # if adj_lst[S] == 0:
        #     return 0
        while True:
            if visited[S] == 0:
                visited[S] = 1
                stack.append(S)
                for w in adj_lst[S]:
                    if visited[w] == 0:
                        S = w
                        break
            else:
                if stack:
                    S = stack.pop()
                else:
                    break
        print(visited)
        if visited[G] == 1:
            return 1

    print(f'#{tc} {dfs(S, G)}')

import sys
sys.stdin = open('input.txt', 'r')

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))
    graph = []
    parents = list(range(N+1))
    for i in range(M):
        graph.append((info[i*2], info[i*2+1]))
    
    for s, e in graph:
        s_root = find(s)
        e_root = find(e)
        if s_root != e_root:
            parents[s_root] = e_root
            
    ans = set()
    for i in range(1, N+1):
        ans.add(find(i))
    print(ans)

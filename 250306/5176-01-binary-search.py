def make_tree(n):
    cl = n
    cr = n+1
    if cl/ 2 == cr//2:
        p = cl // 2
        if p and cl < p:
            tree[cl], tree[p] = tree[p], tree[cl]

        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    for i in range(1, N+1):
        make_tree(i)
    

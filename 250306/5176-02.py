def make_tree(i):
    global cnt

    left = i*2
    right = i*2+1
    if left <= N:
        make_tree(left)

    cnt += 1
    tree[i] = cnt 
    
    if right <= N:
        make_tree(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 0
    make_tree(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")
    
'''
1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2'''
for _ in range(10):
    tc = input() 
    arr = [list(map(int, input().split())) for _ in range(100)]
    for c in range(100):
        if arr[99][c] == 2:
            sc = c
    sr = 99
    while sr > 0:
        if 0 <= sc-1 and arr[sr][sc-1] == 1:
            while 0 <= sc-1 and arr[sr][sc-1] == 1:
                sc -= 1
        elif sc + 1 < 100 and arr[sr][sc+1] == 1:
            while sc + 1 < 100 and arr[sr][sc+1] == 1:
                sc += 1
        sr -= 1
    print(f'#{tc} {sc}')

    
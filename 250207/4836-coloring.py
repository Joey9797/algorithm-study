import pprint
'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for n in range(N):
        lst = list(map(int, input().split()))

        r1 = lst[0]
        c1 = lst[1]
        r2 = lst[2]
        c2 = lst[3]
        color = lst[-1]
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if arr[r][c] == color:
                    continue
                else:
                    arr[r][c] += color

    # pprint.pprint(arr)
    c = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                c += 1
    print(f'#{tc} {c}')
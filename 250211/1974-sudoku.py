'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
0
7 3 6 4 8 9 2 5 1
8 5 2 7 3 1 6 9 4
9 1 4 5 6 2 7 3 8
4 9 7 2 5 6 8 1 3
5 6 3 1 8 7 9 4 2
2 8 1 9 4 3 5 6 7
6 7 5 3 2 4 1 8 9
1 4 9 6 7 8 3 2 5
3 2 8 1 9 5 4 7 6
'''
N = 9
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        if len(set(list(arr[i][:]))) < 9:
            break
    else: count += 1

    for j in range(N):
        column = [arr[i][j] for i in range(N)]
        if len(set(column)) < 9:
            break
    else: count += 1

    for t in range(3):
        lst = []
        for i in range(3*t, 3 + 3*t): # start 값 (0,
            for j in range(3):
                lst.append(arr[i][j])
        if len(set(lst)) < 9:
            break

        lst = []
        for i in range(3*t, 3 + 3*t): # start 값 (0,
            for j in range(3, 6):
                lst.append(arr[i][j])
        if len(set(lst)) < 9:
            break

        lst = []
        for i in range(3 * t, 3 + 3 * t):  # start 값 (0,
            for j in range(6, 9):
                lst.append(arr[i][j])
        if len(set(lst)) < 9:
            break
    else: count += 1

    if count == 3:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')

# 축구장 LED
'''
4
5 3
35 39
93 70
569 138
'''
import pprint


T = int(input())
for tc in range(1, T+1):
    n, k = list(map(int, input().split()))
    arr = [[0]*n for _ in range(4)]
    t = 1
    while t < k+1:
        for r in range(4):
            for c in range(n):
                if (r + c + 1) % t == 0:
                    if arr[r][c] == 0:
                        arr[r][c] = 1
                    else:
                        arr[r][c] = 0
        t += 1
    cnt = 0
    for r in range(4):
        for c in range(n):
            if arr[r][c] == 1:
                cnt += 1
    # pprint.pprint(arr, width=30) 
    print(f"#{tc} {cnt}")
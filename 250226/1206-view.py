'''
10
0 0 254 185 76 227 84 175 0 0
10
0 0 251 199 176 27 184 75 0 0
11
0 0 118 90 243 178 99 100 200 0 0
'''
T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        max_b = 0
        for j in range(1, 3):
            if buildings[i] < buildings[i-j] or buildings[i] < buildings[i+j]:
                break
        else:
            for jj in range(1, 3):
                if max_b < buildings[i-jj]:
                    max_b = buildings[i-jj]
                if max_b < buildings[i+jj]:
                    max_b = buildings[i+jj]
            view = buildings[i] - max_b
            cnt += view
    print(f'#{tc} {cnt}')

        

        # if buildings[i-2] > buildings[i]:
        #     continue
        # if buildings[i-1] > buildings[i]:
        #     continue
        # if buildings[i+1]
'''
3
4 3 7
2 5 6
1 0 8
'''

# 기준값(기본 r, c) 에서 델타를 사용하여 상하좌우로 가장 작은 값을 찾는다. minr, minc
# 기준값을 minr, minc 로 바꾸고, 카운트 +1을 해준다. 이후 델타를 사용하여 다시 가장 작은 값을 찾는다.
# 만약 더 이상 작은 값이 없다면, 카운트를 총카운트 리스트에 저장하고 break 한다. 다음 r c 를 살펴본다.
# 총카운트 리스트 중 max값 +1이 답.

N = 3
arr = [[4, 3, 7], [2, 5, 6], [1, 0, 8]]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt_l = []
for r in range(N):
    for c in range(N):
        cnt = 0
        sr, sc = r, c
        while 0 <= sr < N and 0 <= sc < N:
            minr, minc = sr, sc
            d_cnt = 4
            for i in range(4):
                nr = sr + dr[i]
                nc = sc + dc[i]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < arr[minr][minc]:
                    minr, minc = nr, nc
                    d_cnt -= 1
            if d_cnt == 4:
                cnt_l.append(cnt)
                cnt = 0
                break
            sr, sc = minr, minc
            cnt += 1
print(cnt_l)
# [1, 2, 1, 0, 3, 0, 1, 4, 1]
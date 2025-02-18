'''
3
2 1 2
5 8 5
7 2 2
'''


def f(i, N):  # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    if i == N:  # 같아지면
        s = 0
        for j in range(N):  # j행에서 고른 열 p[j]
            s += arr[j][p[j]]
        if min_v > s:
            min_v = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]  # 자리교환
            f(i + 1, N)  # i+1자리 결정
            p[i], p[j] = p[j], p[i]  # 원상복구


N = int(input())  # 배열의 크기 N x N
arr = [list(map(int, input().split())) for _ in range(N)]

p = [i for i in range(N)]  # i에서 고른 열 번호
min_v = 10000

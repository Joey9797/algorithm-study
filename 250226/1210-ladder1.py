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
for tc in range(1): # 10개의 테스트케이스가 그냥 주어짐
    input() # 첫번째 줄은 단지 테스트케이스 번호이므로 무시!!!!

    arr = [list(map(int, input().split())) for _ in range(10)]

    # 2의 좌표(마지막 점)를 찾는다
    endR, endC = -1, -1
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 2:
                endR, endC = r, c
    
    r, c = endR, endC # 사다리의 끝점으로 시작점(r, c) 초기화

    # r = 99, c = ?
    while r > 0: # r =0일 때 종료, 그 외에는 반복
        # 좌우를 먼저 검사한다
        # 좌: c-1
        # 우: c+1
        # 2차원 배열 경계조건(0<= r,c <100)에 유의하여야 함
        if c-1 >= 0 and arr[r][c-1] == 1: # 왼쪽으로 이동할 수 있다면.
            while c-1 >= 0 and arr[r][c-1]==1: # 왼쪽으로 감
                c -= 1
        elif c+1 < 10 and arr[r][c+1] == 1: # 오른족으로 이동할 수 있다면
            while c+1 <10 and arr[r][c+1]==1:
                c += 1
        r -= 1
    
    print(f"#{tc} {c}")

# for _ in range(1):
#     case = input()
#     ladder = [''.join(input().split()) for _ in range(10)]
#     er, ec = -1, -1
#     for r in range(10):
#         for c in range(10):
#             if ladder[r][c] == '2':
#                 er, ec = r, c
#     sr, sc = er, ec
#     while sr > 0:
#         if sc + 1 < 10 and ladder[sr][sc+1] == '1':
#             while sc + 1 < 10 and ladder[sr][sc+1] == '1':
#                 sc += 1
#         if 0 <= sc - 1 and ladder[sr][sc-1] == '1':
#             while 0 <= sc - 1 and ladder[sr][sc-1] == '1':
#                 sc -= 1
#         else:
#             sr =- 1

#     print(f"#{case} {sc}")

'''
1 = 1
2 = 5, 7, 3
3 = 9, 11, 5
4 = 13, 15, 7'''
M = int(input())
N = (M-1)*4 + 1
arr_0 = ['*'] * N   # 짝수일 때
arr_1 = ['*'] + [' '] * (N-1)   # 홀수일 때

if M == 1:
    print('*')
elif M == 2:
    print(''.join(arr_0))   # 첫번째줄(0번줄)
    print(''.join(arr_1))   # 두번째줄(1번줄)
    arr_0[1] = ' '  # 세번째줄(2번줄)
    print(''.join(arr_0))  

    mid_r = (N+2) // 2  # 행 중간값(세로 중앙값)
    mid_c = N // 2      # 열 중간값(가로 중앙값)
    for r in range(3, N+2):
        if r <= mid_r+1:        
            if r % 2 == 0:      # 짝수일 때     
                arr_0[r - 1] = ' '
                arr_0[N - (r-2)] = ' '
                print(''.join(arr_0)) 
            if r % 2 == 1 :      # 홀수일 때
                arr_1[r + 1] = '*'
                arr_1[N - r] = '*'
                print(''.join(arr_1)) 
        else:
            if r % 2 == 0:      # 짝수일 때     
                arr_0[mid_c - (r - mid_r-2)] = '*'
                arr_0[mid_c + (r - mid_r-2)] = '*'
                print(''.join(arr_0)) 
            if r % 2 == 1:      # 홀수일 때
                arr_1[mid_c - (mid_r+2 - r)] = ' '
                arr_1[mid_c + (mid_r+2 - r)] = ' '
                print(''.join(arr_1)) 
else:
    print(''.join(arr_0))   # 첫번째줄(0번줄)
    print(''.join(arr_1))   # 두번째줄(1번줄)
    arr_0[1] = ' '  # 세번째줄(2번줄)
    print(''.join(arr_0))  

    mid_r = (N+2) // 2  # 행 중간값(세로 중앙값)
    mid_c = N // 2      # 열 중간값(가로 중앙값)
    for r in range(1, N+2):
        if r <= mid_r+1:        
            if r % 2 == 0 and r > 2:      # 짝수일 때     
                arr_0[r - 1] = ' '
                arr_0[N - (r-2)] = ' '
                print(''.join(arr_0)) 
            if r % 2 == 1 :      # 홀수일 때
                arr_1[r + 1] = '*'
                arr_1[N - r] = '*'
                print(''.join(arr_1)) 
        else:
            if r % 2 == 0:      # 짝수일 때     
                arr_0[mid_c - (r - mid_r-2)] = '*'
                arr_0[mid_c + (r - mid_r-2)] = '*'
                print(''.join(arr_0)) 
            if r % 2 == 1:      # 홀수일 때
                arr_1[mid_c - (mid_r+2 - r)] = ' '
                arr_1[mid_c + (mid_r+2 - r)] = ' '
                print(''.join(arr_1)) 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    for i in range(N-1):
        for j in range(i+1, N):
            x = arr[i] * arr[j]
            x1 = x % 10     # 맨 끝 숫자 
            x2 = x // 10    # 나머지 숫자
            if x1 != 0:
                while x2 > 0:
                    x11 = x2 % 10   # 그 전 숫자
                    x22 = x2 // 10  # 나머지 숫자
                    if x1 < x11:
                        break
                    else:
                        x1 = x11
                        x2 = x22
                else:
                    if max_v < x:
                        max_v = x
    result = max_v
    if max_v == 0:
        result = -1
    print(f"#{tc} {result}")
        
                

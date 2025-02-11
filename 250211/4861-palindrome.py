T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [[char for char in input()] for _ in range(N)]

    k = M // 2
    def find_palindrome(N, k, arr):
        for i in range(N):
            for j in range(N - M + 1):
                for m in range(k):
                    if arr[i][j + m] != arr[i][j + M - 1 - m]: # (i,j) 기준점 + m 번째 글짜 같지 않다.
                        break
                else:  # (i,j) 기준점 + m 번째 글짜 같다. ex) (0,4) 기준점, 0번째 검사중 양끝의 B가 같음
                    return i, j, 0
        for j in range(N):
            for i in range(N - M + 1):
                for m in range(k):
                    if arr[i + m][j] != arr[i + M - 1 - m][j]:
                        break
                else:
                    return i, j, 1

    result = find_palindrome(N, k, arr)
    if result[-1] == 0:
        i, j, n = result
        palindrome = arr[i][j:j+M]
    else:
        i, j, n = result
        palindrome = []
        for m in range(M):
            ii = i
            ii += m
            palindrome.append(arr[ii][j])
    print(f"#{tc} {''.join(palindrome)}")

'''
1
3
9 4 7
8 6 5
5 3 7'''
def find_sum(r, total):
    global min_sum

    if r == N:
        min_sum = min(min_sum, total)
        return 
    else:
        for c in range(N):
            if visited[c] == 0:
                visited[c] = 1
                find_sum(r+1, total+arr[r][c])
                visited[c] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 30
    find_sum(0, 0)
    print(f"#{tc} {min_sum}")
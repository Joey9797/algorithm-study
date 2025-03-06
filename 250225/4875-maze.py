'''
1
5
13101
10101
10101
10101
10021
'''
def find_way(r, c, maze, visited):
    if maze[r][c] == '3':
        return 1
    
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and (maze[nr][nc] == '0' or maze[nr][nc] == '3'):
            visited[nr][nc] = 1
            result = find_way(nr, nc, maze, visited)
            if result == 1:
                return 1

    return 0
                

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                sr, sc = r, c
                visited[sr][sc] = 1

    result = find_way(sr, sc, maze, visited)
    print(f'#{tc} {result}')
    
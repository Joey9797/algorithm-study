import sys
sys.stdin = open('input.txt', 'r')

# memoization(dp) 배열에 거리값을 저장하여 재활용하자.
# 1. 현재 노드에서 탐색가능한 노드들을 찾는다.
# 2. 가능한 노드 중 하나를 골라(for 문을 통해) 함수를 재귀호출한다.
# 3. 막다른 길이 나올 때까지 전진하며 dp에 visited(1) 처리를 해준다.
# 4. 막다른 길이 나오면, 현재 노드의 값을 리턴한다. 리턴하며 +1 처리를 해준다. (전진한 만큼 더해주기)
# 5. 리턴한 값은 이전 함수의 노드값과 비교된다. 더 큰 값이 해당 노드의 값이 된다.
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
def dfs(sr, sc, cnt, worked):   # worked: 공사 여부
    global max_cnt

    visited[sr][sc] = 1

    if max_cnt < cnt:
        max_cnt = cnt

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        # 범위 벗어났거나, 이미 방문했던 정점일 시 continue
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
            continue

        # 다음 정점이 현재 정점보다 작으면 재귀호출
        if map_info[nr][nc] < map_info[sr][sc]:
            dfs(nr, nc, cnt+1, worked)
            visited[nr][nc] = 0

        # 아직 공사를 안했고, 다음 정점이 현재 정점보다 작거나 같을 때
        elif not worked and map_info[nr][nc] >= map_info[sr][sc]:
            cut = map_info[nr][nc] - map_info[sr][sc] + 1
            if cut <= K:    # 깎아야할 높이가 K보다 작거나 같으면 재귀호출
                map_info[nr][nc] -= cut
                dfs(nr, nc, cnt+1, True)
                map_info[nr][nc] += cut
                visited[nr][nc] = 0
    visited[sr][sc] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_info = [[*map(int, input().split())] for _ in range(N)]
    max_cnt = 0
    visited = [[0]*N for _ in range(N)]

    # 최대 높이 찾기
    max_h = 0
    for r in range(N):
        for c in range(N):
            if map_info[r][c] > max_h:
                max_h = map_info[r][c]
    
    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if map_info[r][c] == max_h:
                dfs(r, c, 1, False)

    print(f"#{tc} {max_cnt}")
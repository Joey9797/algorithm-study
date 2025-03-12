from collections import deque
import sys
sys.stdin = open("input.txt", "r")

'''
while 문으로 구현 실패
'''
# visit:현재까지 방문한 방 개수, room_num: 현재 내가 있는 방 번호, battery:배터리 사용량
'''
1. 다음으로 갈 방 고르고 다음방 visited 처리
2. 그 방으로 갈 때 필요한 사용량 더하기
3. 다음 방으로 이동 
4. 위 1~3번 반복
5. 현재까지 방문한 방 개수가 N이 되면, 0번 방으로 돌아가서 사용량 더하기
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 관리구역의 마지막번호
    data = [[*map(int, input().split())] for _ in range(N)]
    visited = [1]+[0]*(N-1) # 방문한 방 번호 표시
    min_battery = float('inf')
    room_num = 0    # 현재 방 번호
    prev_room_num = 0   # 이전 방 번호
    Q = deque()
    while Q:
        if visited[room_num] == N:

        for c in range(1, N):
            if visited[c] == 0:
                visited[c] = visited[room_num] + 1
                Q.append(c)
        else:
            room_num = Q.popleft()
    print(f"#{tc} {total}")
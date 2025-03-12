import sys
sys.stdin = open("input.txt", "r")

# visit:현재까지 방문한 방 개수, room_num: 현재 내가 있는 방 번호, battery:배터리 사용량
'''
1. 다음으로 갈 방 고르고 다음방 visited 처리
2. 그 방으로 갈 때 필요한 사용량 더하기
3. 다음 방으로 이동 
4. 위 1~3번 반복
5. 현재까지 방문한 방 개수가 N이 되면, 0번 방으로 돌아가서 사용량 더하기
'''
def rotate(room_num, battery):
    global total 

    if visited[room_num] == N-1:
        battery += data[room_num][0]
        total = min(total, battery)
        return
    
    for c in range(1, N):   # 다음으로 갈 방 고르기
        if visited[c] == 0:
            visited[c] = visited[room_num]+1
            rotate(c, battery+data[room_num][c])
            visited[c] = 0
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 관리구역의 마지막번호
    data = [[*map(int, input().split())] for _ in range(N)]
    visited = [0]*N     # 방문한 방 번호 표시
    total = float('inf')
    rotate(0, 0)
    print(f"#{tc} {total}")
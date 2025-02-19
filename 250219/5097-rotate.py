T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    Q = list(map(int, input().split())) + [0]
    N += 1

    for _ in range(M):
        Q[N-1] = Q[0]
        Q[:N-2] = Q[1:N-1]
        Q[N-2] = Q[N-1]
    print(f'#{tc} {Q[0]}')

#---------------------------------------------------------------------
# deque 클래스로 deque 객체 만들어서 사용

# from collections import deque

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     num = list(map(int, input().split()))
#     q = deque()
#     q.extend(num)
#
#     for _ in range(M):
#         q.append(q.popleft())
#
#     print(f'#{tc} {q[0]}')
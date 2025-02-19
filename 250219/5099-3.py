from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    che = list(map(int, input().split()))
    num = [i for i in range(1, M+1)]
    piz = {}
    for c, n in list(zip(num, che)):
        piz[c] = n

    ov = deque()
    ov.extend(i for i in range(1, N+1))
    f = N

    while len(ov) > 1:
        if f < M and piz[ov[0]] // 2 == 0:
            piz[ov[0]] //= 2
            f += 1
            ov[0] = f
            ov.append(ov.popleft())
        elif piz[ov[0]] // 2 > 0:
            piz[ov[0]] //= 2
            ov.append(ov.popleft())
        elif f == M and piz[ov[0]] // 2 == 0:
            ov.popleft()

    print(f'#{tc} {ov[0]}')
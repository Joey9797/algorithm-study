'''
1
5 3 2
4 1
5 2
3 3
'''

T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))   #노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    arr = [0] * (N+1)
    for _ in range(M):
        c, v = list(map(int, input().split()))
        arr[c] = v
    for i in range(N, 0, -1):
        p = i // 2
        arr[p] += arr[i]
    print(f'#{tc} {arr[L]}')
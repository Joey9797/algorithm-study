'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40'''
def min_heap(i):
    heap[i] = info[i-1]
    p = i // 2
    c = i
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = list(map(int, input().split()))
    heap = [0] * (N+1)
    for i in range(1, N+1):
        min_heap(i)
    sum_v = 0
    last = N
    while last > 0:
        last //= 2
        sum_v += heap[last]
    print(f"#{tc} {sum_v}")
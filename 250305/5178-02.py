'''
1
5 3 2
4 1
5 2
3 3
'''
def fill_tree(i):   # 이진트리 비어있는 곳 채우기
    left = i*2
    right = i*2+1

    if left <= N:
        fill_tree(left)
        arr[i] += arr[left]
    if right <= N:
        fill_tree(right)
        arr[i] += arr[right]

T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))   #노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    arr = [0] * (N+1)
    for _ in range(M):  # 트리에 값 저장 완료
        c, v = list(map(int, input().split()))
        arr[c] = v
    fill_tree(1)
    print(f"#{tc} {arr[L]}")
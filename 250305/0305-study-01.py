# 이진트리 배열에 저장하기

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):   # 전위순회(부모 먼저 처리)
    if T:   # 들어온 정점이 0이 아니면 (존재하는 정점이라면)
        print(T, end = ' ') # 부모 처리
        pre_order(left[T])  # 왼쪽자식으로 이동
        pre_order(right[T]) # 오른쪽자식으로 이동

N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장할 배열 / N+1 하는거 명심!! (0부터 N까지니까까)
right = [0]*(N+1)       # 
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장할 배열

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p]==0:      # 왼쪽자식이 아직 없으면
        left[p] = c     # 부모를 인덱스로 자식 저장
    else:               # 왼쪽자식이 있으면
        right[p] = c    # 오른족에 저장
    par[c] = p          # 자식을 인덱스로 각 자식의 부모 저장 

# 루트 찾기
root = 1
for i in range(1, N+1):
    if par[i] == 0:
        root = i
        break

# 조상 찾기
c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)
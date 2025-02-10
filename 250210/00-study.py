# def seq_search(N, arr, key):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == key:
#                 return 1
#     return 0
#
# N = 3
# key = 5
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(seq_search(N, arr, key))


#-----------------------------------------------------------------------------
# 순차검색
# for 문
# def seq_search(a, n, key):
#     for i in range(n):
#         if a[i] == key:
#             return i
#         elif a[i] > key:
#             return -1
#     return -1   # 모든 원소가 key보다 작으면 -1 리턴해라

# arr = [4, 9, 11, 23, 2, 19, 7]
# arr.sort()
# print(arr)
# print(seq_search(arr, len(arr), 11))
# print(seq_search(arr, len(arr), 100))


#-----------------------------------------------------------------------------
# 순차검색
# while 문
# def seq_search(a, n, key):
#     i = 0
#     while i < n and a[i] < key:
#         i += 1
#     if i
# arr = [4, 9, 11, 23, 2, 19, 7]
# arr.sort()
# print(arr)
# print(seq_search(arr, len(arr), 11))
# print(seq_search(arr, len(arr), 100))


#-----------------------------------------------------------------------------
# 이진탐색
# while 문
def binary_search(a, n, key):
    start = 0   # 검색 구간 설정
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:    # middle 값이 key 와 같은 경우
            return middle           #
        elif a[middle] > key:   # middle 값이 key 보다 큰 경우
            end = middle - 1
        else:                   # middle 값이 key 보다 작은 경우
            start = middle + 1
    return -1   # 검색구간이 남아있지 않으면(while 문이 끝나면) -1 리턴

arr = [2, 4, 7, 9, 11, 19, 23]
print(binary_search(arr, len(arr), 11))
print(binary_search(arr, len(arr), 10))



#-----------------------------------------------------------------------------
# 선택정렬
# for 문
# def selection_sort(a, N):
#     for i in range(N-1):    # start 값 범위
#     # start 값은 맨 끝 idx까지 갈 필요가 없다. 어차피 맨 끝은 하나니까 최솟값이 없음.
#     # 때문에 N-1 (index 끝에서 두번째) 까지만 start값이 있으면 된다.
#         min_idx = i         # 최솟값 인덱스 초기화, 구간의 맨 앞 원소를 일단 넣어둔다.
#         for j in range(i+1, N):  # start ~ 끝 범위에서 최솟값 찾는다.
#         # i+1 부터 시작하는 이유는 i(초기값) 와 i+1 을 비교해야 하기 때문.
#             if a[min_idx] > a[j]:   # 만약 a[j]가 min보다 작다면
#                 min_idx = j         # min 값에 j를 넣는다.
#         a[i], a[min_idx] = a[min_idx], a[i]
#
# arr = [10, 25, 64, 22, 11]
# selection_sort(arr, len(arr))
# print(arr)



#-----------------------------------------------------------------------------
# 셀렉션 알고리즘
k = 3 # k번째로 작은 원소 (3번째로 작은 원소 / 5)
def select(arr, k):
    for i in range(0, k):   # k번째로 작다는건 이쁜 정렬의 k-1 번째를 뜻한다.
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]

arr = [5, 3, 4, 7, 6]
print(select(arr, k))
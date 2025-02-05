# '''
# 6
# 2 7 5 3 1 7
# '''
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# # 합 구하기
# s = 0
# for i in range(N):
#     s += arr[i]
#
# print(s)
#
# # 최댓값의 인덱스 찾기
# max_idx = 0
# for i in range(1, N):
#     if arr[i] >= arr[max_idx]:
#         max_idx = i
# print(max_idx)

# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기
'''
6
5
2 7 5 3 1 5
'''
N = int(input())
V = int(input())
arr = list(map(int, input().split()))

def find_index(N, V, arr):
    idx = -1
    for i in range(N):
        if V == arr[i]:
            idx = i
            break
    return idx

print(find_index(N, V, arr))
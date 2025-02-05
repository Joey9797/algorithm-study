N = int(input())
arr = list(map(int, input().split()))

# 낙차가 가장 큰 상자 구하기
def find_box(N, arr):
    count_list = []
    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if arr[j] < arr[i]:
                count += 1
        count_list.append(count)
    return max(count_list)

result = find_box(N, arr)
print(result)

'''
9
7 4 2 0 0 6 0 7 0

max_v = 0
for i in range(N-1): # 마지막 원소는 자기 뒤에 비교할 값이 없기 때문에 자연히 낙차가 0이 됨.
    cnt = 0         # i박스 오른쪽(i+1~N-1)에 더 낮은 박스 개수 (낙차)
    for j in range(i+1, N):
        if box[i] > box[j]:
            cnt += 1    # 더 낮은 박스면 낙차 추가
    if max_v < cnt:
        max_v = cnt
print(max_v)
'''
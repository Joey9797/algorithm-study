'''
5
55 7 78 12 42
'''
N = int(input())
arr = list(map(int, input().split()))

def bubblesort(N, arr):
    # i는 구간을 정하는 변수. 따라서 끝(N-1)에서부터 0 직전까지 점점 줄여가는 첫 반복문을 작성
    # i는 인덱스가 아니라, 그냥 숫자(범위)다.
    for i in range(N-1, 0, -1):
        # range(i), 여기서 i가 구간을 의미함을 알 수 있음
        for j in range(i):
         # j는 i(구간 길이) 내에서 인덱스를 반복해서 꺼내옴
            # 0 ~ i-1 내에서 큰 값을 계속 오른쪽으로 옮기라는 뜻
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubblesort(N, arr))


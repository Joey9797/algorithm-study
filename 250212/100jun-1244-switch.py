B = int(input()) # 버튼의(스위치)의 개수
arr = [0] + list(map(int, input().split()))
N = len(arr)    # 0 + 스위치 배열의 길이
S = int(input())    # 학생 수
s_info = [list(map(int, input().split())) for _ in range(S)] # 학생 별 정보

for info in s_info:
    if info[0] == 1:
        for i in range(1, N, 3):
            if i % info[1] == 0 and i > 0:
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
    elif info[0] == 2:    # [2, 3]
        mid = info[1] # 중심 스위치
        if arr[mid] == 0:
            arr[mid] = 1
        else:
            arr[mid] = 0
        i = 1
        while mid - i > 0 and mid + i < N:
            if arr[mid - i] == arr[mid + i]:
                if arr[mid - i] == 0:
                    arr[mid - i] = 1
                elif arr[mid - i] == 1:
                    arr[mid - i] = 0
                if arr[mid + i] == 1:
                    arr[mid + i] = 0
                elif arr[mid + i] == 0:
                    arr[mid + i] = 1
                i += 1
            else:
                break

ans = [arr[i:i+20] for i in range(1, N, 20)]
for line in ans:
    print(' '.join(list(map(str, line))))
B = int(input()) # 버튼의(스위치)의 개수
arr = [0] + list(map(int, input().split()))
N = len(arr)    # 0 + 스위치 배열의 길이
S = int(input())    # 학생 수
s_info = [list(map(int, input().split())) for _ in range(S)] # 학생 별 정보

for info in s_info:
    if info[0] == 1:
        for i in range(N):
            if i % info[1] == 0 and i > 0:
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
    if info[0] == 2:    # [2, 3]
        if arr[info[1]] == 0:
            arr[info[1]] = 1
        else:
            arr[info[1]] = 0
        for i in range(1, N):
            if arr[info[1] - i] != arr[info[1] + i]:
                break
            else:
                if arr[info[1] - i] == 0 and info[1] - i > 0 :
                    arr[info[1] - i] = 1
                elif arr[info[1] - i] == 1 and info[1] - i > 0 :
                    arr[info[1] - i] = 0
                if arr[info[1] + i] == 1 and info[1] - i > 0:
                    arr[info[1] + i] = 0
                elif arr[info[1] + i] == 0 and info[1] - i > 0:
                    arr[info[1] + i] = 1

ans = [arr[i:i+20] for i in range(1, N, 20)]
result = ' '.join(list(map(str, ans[0])))
print(result)
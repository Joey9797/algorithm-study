# 공 받은 횟수 홀수: +L
# 공 받은 횟수 짝수: -L
N, M, L = list(map(int,input().split())) # 자리수 N, 공 받는 횟수 M, 공 던지는 거리 L
arr = [0] * (N)
i = 0
arr[0] = 1
cnt = 0
while M not in arr:
    if arr[i] % 2 == 0:
        arr[(i-L+N) % N] += 1
        i = (i-L+N) % N
        cnt += 1
    elif arr[i] % 2 == 1:
        arr[(i+L) % N] += 1
        i = (i+L) % N
        cnt += 1
print(cnt)

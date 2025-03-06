def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    if i == N:  #
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]  # 자리교환
            f(i+1, N)   # i+1자리 결정
            p[i], p[j] = p[j], p[i]  # 원상복구

p = [0,1,2]
N = 3
# f(0, N)

arr = [0, 2, 1]
i = 0
while 3 not in arr:
    arr[i] += 1
    i += 1
    print(arr)
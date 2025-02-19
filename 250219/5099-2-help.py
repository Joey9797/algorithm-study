from collections import deque

N, M = list(map(int, input().split()))
che = list(map(int, input().split()))
num = [i for i in range(1, M+1)]
piz = {}
for c, n in list(zip(num, che)):
    piz[c] = n
# {1: 7, 2: 2, 3: 6, 4: 5, 5: 3}
def bake_piz(o):  # 오븐에서 피자 굽기
    global f
    for p in o:
        piz[p] //= 2
    for i in range(len(ov)):
        if piz[o[i]] == 0:
            if f < M:
                f += 1
                o[i] = f
            else:
                o.remove(ov[i])
    if len(o) == 1:
        return o[0]
    else:
        return bake_piz(o)

ov = [0] * N
f = 0
for i in range(N): # 오븐에 첫 피자 넣기
    f += 1
    ov[i] = f
result = bake_piz(ov)
print(result)





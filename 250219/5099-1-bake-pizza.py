from collections import deque

# 피자를 오븐에 넣는다.
# 오븐에서 치즈가 0이 될때까지 //2를 해준다.
# 오븐에서 치즈가 0인 피자가 입구로 올 때까지 돌려준다.
# 치즈가 0인 피자를 꺼내고, 다음 피자를 넣는다.
# 치즈가 0인 피자가 또 있다면, 또 화덕을 돌려준다.
# 치즈가 0인 피자를 꺼내고, 다음 피자를 넣는다. 치즈가 0인 피자가 없을때까지 반복한다.
# 새로 넣은 피자들로 그걸 또 치즈가 0이 될때까지 돌린다.
#
def melt_cheese(ov, N): # 오븐에 들어간 피자 치즈 녹이기
    is_melted = False
    for i in range(N):
        ov[i] //= 2
    for p in ov:
        if p == 0:
            is_melted = True
            break
    if is_melted:
        return ov
    else:
        return melt_cheese(ov, N)

N, M = list(map(int, input().split()))
piz = list(map(int, input().split()))
#[7 2 6 5 3]
ov = [0] * N    #[0, 0, 0]
ov_idx = [0] * N    #[0, 0, 0]
f = 0
r = M

for i in range(N):  # 첫 피자 N개(3개) 오븐에 넣기
    f += 1
    ov[i] = piz[f]  #[7, 2, 6]
    ov_idx[i] = f   #[0, 1, 2]
melt_cheese(ov, N)  #[1, 0, 1]
n_ov = deque()
n_ov.extend(ov_idx) #[1, 0, 1] index 넣었음
while f < r:
    for j in range(N):  # 새 피자 오븐에 넣기
        n_ov.append(n_ov.popleft()) #[1, 2, 0]  #[2, 0, 0]
        if ov[n_ov[0]] == 0:        #[0, 1, 1]
            f += 1  # f = 3
            n_ov[0] = f #[3, 2, 0] /ov = [5, 1, 1]
            continue
    melt_cheese(ov, N)  #[2, 0, 0]
melt_cheese(ov, N)

print(melt_cheese(ov, N))
# print(ov)


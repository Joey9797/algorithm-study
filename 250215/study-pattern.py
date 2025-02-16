p = list('XYPV')
txt = list('EOGGXYPVSY')
N = len(txt)
M = len(p)
ans = []
#-------------------------------------------------------------------------
# 패턴이 있는지만 찾고, 패턴이 있는 가장 첫번째 인덱스 뽑기 (else 없음)
i = j = 0
while i < N and j < M:
    if p[i] != txt[j]:
        i = i-j # 무조건 아래줄의 i += 1 가 실행되므로, i-j 를 해줘야 i-j+1 이 된다.
        j = -1  # 무조건 아래줄의 j += 1 가 실행되므로, j를 0으로 돌리고 싶다면, j = -1 이라고 해야 함
    i += 1
    j += 1
if j == M:
    result = i - M  # i - j 랑 똑같음


#-------------------------------------------------------------------------
# 패턴이 있는지만 찾고, 패턴이 있는 가장 첫번째 인덱스 뽑기 (else 있음)
i = j = 0
while i < N and j < M:
    if txt[i] != p[j]:
        i = i - j + 1
        j = 0
    else:
        i += 1
        j += 1
if j == M:
    result = i - j


#-------------------------------------------------------------------------
# 패턴이 몇 개 있는지 찾기
p = list('bab')
txt = list('bababab')
N = len(txt)
M = len(p)

i = j = 0
cnt = 0
while i < N:
    if txt[i] != p[j]:
        i = i-j+1
        j = 0
    else:
        i += 1
        j += 1
    if j == M:
        cnt += 1
        i = i-j+1
        j = 0
print(cnt)


#-------------------------------------------------------------------------
# 패턴이 정확히 몇 개 있는지 찾기 (aaa는 aaaaaa안에 2개 있다)
p = list('aaa')
txt = list('aaaaaa')
N = len(txt)
M = len(p)

i = 0
cnt = 0
while i + M <= N:
    if txt[i:i+M] == p:
        cnt += 1
        i = i+M
    else:
        i += 1
print(cnt)


#-------------------------------------------------------------------------
# 사이사이에 값 넣기
# i = 0
# while i < M:
#     ans.extend([p[i], txt[i]])
#     i += 1
# ans.extend(txt[M:])
# print(''.join(ans))



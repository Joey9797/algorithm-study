# 패턴이 몇 개 존재하는지 찾기. 중복되어도 패턴으로 인정
txt = 'bababab'
p = 'bab'
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


# 패턴이 몇 개 존재하는지 찾기. 정확한 패턴 모양이어야 함.
cnt = 0
i = 0
while i + M <= N:
    if txt[i:i+M] != p:
        i += 1
    else:
        i += M
print(cnt)
# 패턴이 존재하는지 찾기. 존재한다면 1과 index 리턴, 아니면 0 리턴
txt = 'aaaaaabaacaaa'
p = 'baa'
N = len(txt)
M = len(p)

i = j = 0
while i < N and j < M:
    if txt[i] != p[j]:
        i = i - j
        j = -1
    i += 1
    j += 1
if j == M:
    result = 1
    index = i - j


i = j = 0
while i < N and j < M:
    if txt[i] != p[j]:
        i = i - j + 1
        j = 0
    else:
        i += 1
        j += 1
if j == M:
    result = 1  # 패턴이 있다
    index = i - j   # 패턴 시작 인덱스
else:
    result = 0

print(result)
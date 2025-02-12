## 패턴 비교 1
t = 'TTTTTATTAATA'  # 풀 텍스트
p = 'TTA'           # 비교할 패턴
N = len(t)
M = len(p)

i = j = 0
while i < N and j < M:  # 패턴
    if t[i] != p[j]:    # 지금 비교중인 범위 내에서 i 가 j 와 다르다면
        i = i - j + 1   # i 에서 j가 이동한 만큼 뺀다.
        # 그리고 i는 오른쪽으로 한 칸 옮겨서 다시 비교를 시작해야 하기 때문에 +1을 해준다.
        j = 0   # j 는 시작점으로 되돌린다.
    else:   # 만약 i와 j가 일치한다면,
        i += 1  # 다음번 i를 비교해야 하므로, i를 1 증가시킨다
        j += 1  # 마찬가지로 j 도 1 증가시킨다.
if j == M:
    print(i - j)
else:
    print('텍스트 내에 패턴이 없습니다.')


## ------------------------------------------------------------------------------------------
## 패턴 비교 2 (패턴이 텍스트 내에 여러개 있을 때)
t = 'TTTTTATTAATA'  # 풀 텍스트
p = 'TTA'           # 비교할 패턴
N = len(t)
M = len(p)

def brutefore(p, t):
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:  # j가 M 길이가 됐을 때도, 계속 비교를 해줘야 하므로, j < M 조건을 뺀다.
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
        if j == M:  # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
        return cnt

    else:
        print('텍스트 내에 패턴이 없습니다.')



## ------------------------------------------------------------------------------------------
## 패턴 비교 3 (for문으로 구성하기)
t = 'TTTTTATTAATA'
p = 'TTA'

def brutefore(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return '텍스트 내에 패턴이 없습니다.'





## ------------------------------------------------------------------------------------------
## KMP 알고리즘
# def kmp(t, p):
#     N = len(t)
#     M = len(p)
#     lps = [0] * (M+1)   # 우선 패턴 내에 또 패턴이 존재하는지를 확인하는 arr를 하나 만든다.
#     # process
#     # 그 arr인 lps를
#     j = 0 # 일치한 개수== 비교할 패턴 위치
#     lps[0] = -1
#     for i in range(1, M):
#         lps[i] = j          # p[i]이전에 일치한 개수
#         if p[i] == p[j]:
#             j += 1
#         else:
#             j = 0
#     lps[M] = j
#     # search
#     i = 0   # 비교할 텍스트 위치
#     j = 0   # 비교할 패턴 위치
#     while i < N and j <= M:
#         if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
#             i += 1
#             j += 1
#         else:               # 불일치
#             j = lps[j]
#         if j==M:    # 패턴을 찾을 경우
#             print(i-M, end = ' ')    # 패턴의 인덱스 출력
#             j = lps[j]
#
#     print()
#     return
#
# t = 'zzzabcdabcdabcefabcd'
# p = 'abcdabcef'
# kmp(t, p)
# t = 'AABAACAADAABAABA'
# p = 'AABA'
# kmp(t, p)
# t = "AAAAABAAABA"
# p =  "AAAA"
# kmp(t, p)
# t = "AAAAABAAABA"
# p =  "AA"
# kmp(t, p)






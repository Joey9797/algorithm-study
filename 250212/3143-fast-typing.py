T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    def typing(a, b):
        N = len(a)
        M = len(b)
        i = 0
        cnt = 0
        while i+M <= N:
            if a[i:i+M] == b:
                cnt += 1
                i += M
            else:
                i += 1
        result = N - cnt * M + cnt
        return result

    print(f'#{tc} {typing(A, B)}')

# T = int(input())
#
# for tc in range(1, T+1):
#     text, pattern = input().strip().split()
#
#     cnt = 0 # 패턴 등장 횟수
#     i = 0
#     while i <= len(text) - len(pattern):
#         if text[i:i+len(pattern)] == pattern: # 만약에 i를 기준으로 패턴 일치
#             cnt += 1 # 카운트를 늘리고
#             # i += 1 # 이렇게 하면 안됨
#             i += len(pattern) # 패턴 길이만큼 건너뛴다.
#         else: # 일치하지 않으면
#             i += 1 # 한 글자씩만 이동(고지식한 패턴매칭처럼)
#     result = len(text) - len(pattern) * cnt + cnt
#
#     print(f"#{tc} {result}")

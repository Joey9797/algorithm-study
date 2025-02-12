T = int(input())
for tc in range(1, T+1):
    str1 = sorted(list(set(list(input()))))
    str2 = sorted(list(input()))
    N = len(str1)
    M = len(str2)
    max_cnt = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if str1[i] == str2[j]:
                count += 1
            else:
                continue
        if count > max_cnt:
            max_cnt = count
    print(f'#{tc} {max_cnt}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_1 = 0
    max_2 = 0
    for num in arr:
        if num < 10 and max_1 <= num:
            max_2 = max_1
            max_1 = num
        if num < 10 and max_2 < num < max_1:
            max_2 = num
        elif num >= 10:
            num = num
            n1 = num % 10   # 일의 자리수
            n2 = num // 10  # 나머지
            while n2 > 10:
                n11 = n1 % 10
                n22 = n2 // 10
                if n1 == 0:
                    break
                elif n11 > n1:
                    break
                else:
                    n1 = n11
                    n2 = n22
            else:
                if n1 < n2:
                    continue
                elif max_1 < num:
                    max_2 = max_1
                    max_1 = num
                elif max_2 < num < max_1:
                    max_2 = num
    result = max_1 * max_2
    if max_1 * max_2 == 0:
        result = -1
    print(f'#{tc} {result}')

    # while 0 < n2 < 10:
    #     n11 = n1 % 10
    #     n22 = n2 // 10
    #     if n1 == 0:
    #         break
    #     elif n11 > n1:
    #         break
    #     else:
    #         n1 = n11
    #         n2 = n22
    #     if max_1 < num:
    #         max_1 = num
    #     if max_2 < num < max_1:
    #         max_2 = num




            # T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     v = []
#     for a in arr:
#         j = a
#         if len(a) == 1:
#             v.append(a)
#         else:
#             for i in range(1, len(a)):
#                 if a[i] < a[i-1]:
#                     break
#             else:
#                 v.append(a)
#     v = sorted(list(map(int, v)))
#     result = v[-1] * v[-2]
#     print(f'#{tc} {result}')


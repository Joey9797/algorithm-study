'''
3
400 300 350
1000 299 578
1000 222 888
'''
T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    P = info[0]
    Pa = info[1]
    Pb = info[2]
    def find_page(P, Pp):
        count = 0
        s = 1
        e = P
        while s <= e:
            c = (s + e) // 2
            if c == Pp:
                count += 1
                break
            elif Pp < c:
                e = c - 1
                count += 1
            else:
                s = c + 1
                count += 1
        return count

    result_a = find_page(P, Pa)
    result_b = find_page(P, Pb)

    def result(a, b):
        if a == b:
            return 0
        elif a < b:
            return 'A'
        elif a > b:
            return 'B'

    final_result = result(result_a, result_b)

    print(f"#{tc} {final_result}")

# def find_page(P, Pa, Pb):
#     count_a = 0
#     count_b = 0
#     max_c = max(count_a, count_b)
#     for i in range(1, P+1):
#         s = 1
#         e = P
#         c = (s + e - 1) // 2
#         if c == Pa:
#             count_a += 1
#             return count_a
#         elif Pa < c:
#             e = c
#             count_a += 1
#         else:
#             s = c
#             count_a += 1
#         if e <= s:
#             break
#         if Pb == c:
#             count_b += 1
#             return max_c
#         elif Pb < c:
#             e = c
#             count_b += 1
#         else:
#             s = c
#             count_b += 1
#     return count_a




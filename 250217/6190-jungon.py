T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    arr_lst = list(map(int, arr))
    print(arr_lst)


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

